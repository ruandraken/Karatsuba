#include <iostream>
#include <cmath>
using namespace std;

// Função para calcular o máximo de dois números
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Função para calcular a multiplicação usando o algoritmo de Karatsuba
int karatsuba(int x, int y) {
    // Se os números forem de um dígito, a multiplicação direta é mais rápida
    if (x < 10 || y < 10) {
        return x * y;
    }

    // Encontrando o tamanho dos números
    int tamanho = max(log10(x) + 1, log10(y) + 1);

    // Dividindo os números ao meio
    int meio = tamanho / 2;

    // Calculando as partes divididas dos números
    int a = x / static_cast<int>(pow(10, meio));
    int b = x % static_cast<int>(pow(10, meio));
    int c = y / static_cast<int>(pow(10, meio));
    int d = y % static_cast<int>(pow(10, meio));

    // Recursivamente calculando os produtos
    int ac = karatsuba(a, c);
    int bd = karatsuba(b, d);
    int ad_plus_bc = karatsuba(a + b, c + d) - ac - bd;

    // Calculando o resultado final usando a fórmula de Karatsuba
    return static_cast<int>(pow(10, 2 * meio)) * ac + static_cast<int>(pow(10, meio)) * ad_plus_bc + bd;
}

int main() {
    int num1, num2;
    cout << "Digite o primeiro número: ";
    cin >> num1;
    cout << "Digite o segundo número: ";
    cin >> num2;

    int resultado = karatsuba(num1, num2);
    cout << "O resultado da multiplicação é: " << resultado << endl;

    return 0;
}

