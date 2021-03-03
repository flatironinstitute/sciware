// right_search.c
// Compile with:
// $ clang -g -o right_search right_search.c

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Find the right-most occurence of `val`
// in array `arr` with length `N`.
// Returns the index of the occurence, or -1 if not found.
int right_search(int val, int *arr, int N){
    for(int i = N; i >= 0; i--){
        if(arr[i] == val){
            return i;
        }
    }
    
    return -1;
}

int main(int argc, char **argv){
    
    // Allocate an array and initialize with values
    // like: arr = np.arange(100)
    int N = 100;
    int *arr = (int *) malloc(N*sizeof(int));
    for(int i = 0; i < 10; i++){
        arr[i] = i;
    }
    
    // Now find the right-most occurence of a value in this array
    int search_val = 0;
    int j = right_search(search_val, arr, N);
    if(j != -1)
        printf("Found value %d at loc %d\n", search_val, j);
    else
        printf("Did not find value %d; got loc %d\n", search_val, j);
    
    return 0;
}
