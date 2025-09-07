*Matrices*

Implemente una clase llamada Matriz para representar el comportamiento de una matriz algebraica.

*Funcionalidades a implementar:*

1. *Representación en cadena de caracteres:* Devuelve una cadena que representa la matriz.
2. *Suma de matrices:* Realiza la suma de dos matrices y devuelve el resultado como una nueva matriz.
3. *Resta de matrices:* Realiza la resta de dos matrices y devuelve el resultado como una nueva matriz.
4. *Multiplicación de matrices:* Multiplica dos matrices y devuelve el resultado como una nueva matriz.
5. *Comparación de matrices:* Permite comparar dos matrices para determinar si una es menor, mayor o igual a la otra (definimos que una matriz es mayor, igual o menor que otra bajo el determinante).
6. *Traza de una matriz:* Permite conseguir la traza de una matriz, que es la suma de los elementos de su diagonal.
7. *Transpuesta de una matriz:* Permite conseguir la transpuesta de una matriz (intercambiar filas y columnas).
8. *Simetría:* Permite conocer si una matriz es simétrica o no.
9. *Ceros:* Implemente un método que reciba una matriz M y devuelva otra matriz M'. La matriz M' se forma a partir de M, manteniendo sus valores originales pero haciendo cero cualquier columna o fila que tenga algún cero.
 
*Ejemplo de uso:*

int[,] matriz1 = {
{1, 2, 3},
{4, 5, 6},
{7, 8, 9}
};

int[,] matriz2 = {
{9, 8, 7},
{6, 5, 4},
{3, 2, 1}
};

Matriz m1 = new Matriz(matriz1);
Matriz m2 = new Matriz(matriz2);

// Representación en cadena de caracteres
Console.WriteLine(m1.ToString());
// Esperado:
// 1 2 3
// 4 5 6
// 7 8 9

// Suma de matrices
Matriz suma = m1 + m2;
Console.WriteLine(suma.ToString());
// Esperado:
// 10 10 10
// 10 10 10
// 10 10 10

// Resta de matrices
Matriz resta = m1 - m2;
Console.WriteLine(resta.ToString());
// Esperado:
// -8 -6 -4
// -2 0 2
// 4 6 8

// Multiplicación de matrices
Matriz producto = m1 * m2;
Console.WriteLine(producto.ToString());
// Esperado:
// 30 24 18
// 84 69 54
// 138 114 90

// Traza de una matriz
int traza = m1.Traza();
Console.WriteLine(traza);
// Esperado: 15

// Transpuesta de una matriz
Matriz transpuesta = m1.Transpuesta();
Console.WriteLine(transpuesta.ToString());
// Esperado:
// 1 4 7
// 2 5 8
// 3 6 9

// Simetría
bool esSimetrica = m1.EsSimetrica();
Console.WriteLine(esSimetrica);
// Esperado: False

// Ceros
int[,] matriz3 = {
{1, 2, 0},
{4, 5, 6},
{7, 0, 9}
};

Matriz m3 = new Matriz(matriz3);
Matriz matrizCeros = Matriz.Ceros(m3);
Console.WriteLine(matrizCeros.ToString());
// Esperado:
// 0 0 0
// 4 0 0
//0 0 
