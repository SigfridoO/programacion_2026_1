// --------  GPIO
// Entradas digitales
int DI_00 = 32;
int DI_01 = 33;

// Salidas Digitales
int DO_00 = 23;

// --------  Señales virtuales
// Entradas
int X_00 = 0;
int X_01 = 0;

// Salidas
int Y_00 = 0;

// Bandera
int M_00 = 0;

void setup() {

  // Configurando pines
  pinMode(DI_00, INPUT);
  pinMode(DI_01, INPUT);
  
  pinMode(DO_00, OUTPUT);
}

void loop() {
// ---------- Programa
M_00 = (X_00 || M_00) && !X_01;
Y_00 = M_00;
  

// Actualizando entradas y salidas
X_00 = digitalRead(DI_00);
X_01 = digitalRead(DI_01);
digitalWrite(DO_00, Y_00);

}
