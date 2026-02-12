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

void setup() {

  // Configurando pines
  pinMode(DI_00, INPUT);
  pinMode(DI_01, INPUT);
  pinMode(DI_02, INPUT);
  pinMode(DI_03, INPUT);
  
  pinMode(DO_00, OUTPUT);

  // Condiciones iniciales
  M_00 = 1;
}

void loop() {
// ---------- Programa

M_01 = (M_00 || M_01) && !X_03;
M_02 = M_01 && (X_01 || M_02)  && !X_02 && !X_00;
Y_00 = M_02;  

// Actualizando entradas y salidas
X_00 = digitalRead(DI_00);
X_01 = digitalRead(DI_01);
X_02 = digitalRead(DI_02);
X_03 = digitalRead(DI_03);

digitalWrite(DO_00, Y_00);

}
