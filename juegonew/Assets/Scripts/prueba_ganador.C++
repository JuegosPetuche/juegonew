#include <iostream>

using namespace std;
bool revisarColumnas(string Matriz[3][3]);
bool revisarFilas(string Matriz[3][3]);
bool revisarDiagonalP(string Matriz[3][3]);
bool revisarDiagonalS(string Matriz[3][3]);

int main(){

    string Matrix[3][3] = { {"X", "O", "O"}, {"X", "O", "O"}, {"O", "X", "X" }};
    short i, j;

    for(i = 0; i < 3; i++){

        for(j = 0; j < 3; j++){

            cout << Matrix[i][j] << " ";
        } 
        cout << "\n";
    }


    if(revisarFilas(Matrix) or revisarColumnas(Matrix) or revisarDiagonalP(Matrix) or revisarDiagonalS(Matrix)){

        cout << "HAY UN GANADOR\n";
    }
    else{

        cout << "NO HAY GANADORES";
    }

}

bool revisarFilas(string Matriz[3][3]) {

    for (short i = 0; i < 3; i++) {

        string anterior = Matriz[i][0];
        short acumulador = 1;

        for (short j = 1; j < 3; j++) {

            if (Matriz[i][j] == anterior) {

                acumulador++;
            } else {
                break;
            }
        }

        if (acumulador == 3) {

            cout << "Hay un ganador en la filas " << i + 1 << " y es " << anterior << " 😁\n";
            return true;
        }
    }
    cout << "No gano nadie ☹️\n";
    return false;
}

bool revisarColumnas(string Matriz[3][3]) {

    for (short i = 0; i < 3; i++) {

        string anterior = Matriz[0][i];
        short acumulador = 1;

        for (short j = 1; j < 3; j++) {

            if (Matriz[j][i] == anterior) {

                acumulador++;
            } else {
                break;
            }
        }

        if (acumulador == 3) {

            cout << "Hay un ganador en la columnas " << i + 1 << " y es " << anterior << " 😁\n";
            return true;
        }
    }
    cout << "No gano nadie ☹️\n";
    return false;
}

bool revisarDiagonalP(string Matriz[3][3]){

    short i;
    i = 0;
    
    string anterior = Matriz[i][i];
    short acumulador = 1;

    for (i; i < 3; i++) {

        if (Matriz[i][i] == anterior) {

            acumulador++;

        }
        else{

            break;
        } 
    }

    if(acumulador == 3) {

        cout << "Hay un ganador en la diagonal principal y es " << anterior << " 😁\n";
        return true;
    }
    cout << "No gano nadie ☹️\n";
    return false;
}

bool revisarDiagonalS(string Matriz[3][3]) {
    string anterior = Matriz[0][2]; // Primer elemento de la diagonal secundaria
    short acumulador = 1;

    for (short i = 1, j = 1; i < 3; i++, j--) {
        if (Matriz[i][j] == anterior) {
            acumulador++;
        } else {
            break;
        }
    }

    if (acumulador == 3) {
        cout << "Hay un ganador en la diagonal secundaria y es " << anterior << " 😁\n";
        return true;
    }

    cout << "No ganó nadie ☹️\n";
    return false;
}