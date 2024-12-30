#include <bits/stdc++.h>

#ifdef GEM5
#include "gem5/m5ops.h"
#endif

void printSolution(int **board, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf(" %d ", board[i][j]);
        printf("\n");
    }
}

bool isSafe(int **board, int row, int col, int N) {
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    for (int i=row, j=col; i>=0 && j>=0; i--, j--)
        if (board[i][j])
            return false;

    for (int i=row, j=col; j>=0 && i<N; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

bool solveNQUtil(int **board, int col, int N) {
    if (col >= N)
        return true;

    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col, N)) {
            board[i][col] = 1;

            if (solveNQUtil(board, col + 1, N))
                return true;

            board[i][col] = 0;
        }
    }

    return false;
}

bool solveNQ(int **board, int N) {


    if (solveNQUtil(board, 0, N) == false) {
        printf("Solution does not exist");
        return false;
    }

    return true;
}

int main(int argc, char *argv[]) {
    // the user needs to input the size of the chessboard
    if (argc == 2) {
        int size = atoi(argv[1]);

        // initialize the board
        int **board = new int*[size];
        for (int i = 0 ; i < size; i++)
            board[i] = new int[size];

        for (int i = 0 ; i < size ; i++) {
            for (int j = 0 ; j < size ; j++) {
                board[i][j] = 0;
            }
        }
#ifdef GEM5
    m5_work_begin(0,0);
#endif
        solveNQ(board, size);
#ifdef GEM5
    m5_work_end(0,0);
#endif
        printSolution(board, size);
    }
    else {
        printf("N-Queens program. Usage \n $ ./queens <chess-board-size>\n");
    }
    return 0;
}
