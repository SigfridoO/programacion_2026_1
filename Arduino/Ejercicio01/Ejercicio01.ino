// --------  GPIO
// Entradas digitales
int DI_00 = 32;
int DI_01 = 33;
int DI_02 = 25;
int DI_03 = 26;

// Salidas Digitales
int DO_00 = 23;

// --------  Señales virtuales
// Entradas
int X_00 = 0;
int X_01 = 0;
int X_02 = 0;
int X_03 = 0;

// Salidas
int Y_00 = 0;

// Bandera
int M_00 = 0;
int M_01 = 0;
int M_02 = 0;

// ---------- Temporizadores

#define  numeroDeTON 16
struct temporizador {
    byte entrada;
    byte salida;
    unsigned long tiempo;
    unsigned long tiempoActual;
} TON[numeroDeTON];
struct temporizadorAux {
    byte bandera;
    unsigned long tiempo_Aux1;
    unsigned long tiempo_Aux2;
} TON_Aux[numeroDeTON];

void actualizarTON (int);

int contador = 0;

void setup() {

  // Configurando pines
  pinMode(DI_00, INPUT);
  pinMode(DI_01, INPUT);
  pinMode(DI_02, INPUT);
  pinMode(DI_03, INPUT);
  
  pinMode(DO_00, OUTPUT);

  // Condiciones iniciales
  M_00 = 1;

  // Temporizadores

    TON[0].tiempo = (unsigned long)  3000;
    TON[1].tiempo = (unsigned long)  1000;
    // Comunicacion Serie
    Serial.begin(115200);

}

void loop() {
// ---------- Programa

//M_01 = (M_00 || M_01) && !X_03;
//M_02 = M_01 && (X_01 || M_02)  && !X_02 && !X_00;
//Y_00 = M_02;  
M_01 = (X_00 || M_01) && !X_01;

TON[0].entrada = M_01;
 actualizarTON(0);
 
 Y_00 = TON[0].salida;

// Contador de 1 segundo
TON[1].entrada = !TON[1].salida;
actualizarTON(1);


if (TON[1].salida) {
  Serial.write(contador);
  contador ++;
}
 

// Actualizando entradas y salidas
X_00 = digitalRead(DI_00);
X_01 = digitalRead(DI_01);
X_02 = digitalRead(DI_02);
X_03 = digitalRead(DI_03);

digitalWrite(DO_00, Y_00);

}









void actualizarTON (int i) {
     if (TON [i].entrada)
   {
        if (!TON_Aux[i].bandera) {
           TON_Aux[i].bandera = true;
           TON_Aux[i].tiempo_Aux1 = millis ();  
        }
        TON_Aux[i].tiempo_Aux2 = millis ();
        TON [i].tiempoActual = TON_Aux[i].tiempo_Aux2 - TON_Aux[i].tiempo_Aux1;

        if (TON [i].tiempoActual > TON [i].tiempo) {
            TON [i].salida = true;
        }
    } else {
        TON [i].salida = false;
        TON_Aux[i].bandera = false;
    }
}
