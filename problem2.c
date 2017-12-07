#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define DEBUG 0

struct dynamic_array {
  int *data;
  int size;
  int capacity;
};

short init_dynamic_array(struct dynamic_array *a){
  a->data = malloc(8 * sizeof(int));
  a->size = 0;
  if(!a->data){
    a->capacity = 0;
    return FALSE;
  }
  a->capacity = 8;
  return TRUE;
}

short expand_dynamic_array(struct dynamic_array *a){
  int *new_data = realloc(a->data, a->capacity * 2 * sizeof(int));
  if(new_data == NULL){
    return FALSE;
  }
  if(DEBUG){
    printf("Old Address: %p, New Address: %p\n", (void*)a->data, (void*)new_data);
  }
  a->data = new_data;
  a->capacity = a->capacity * 2;
  if(DEBUG){
    printf("New capacity: %d\n", a->capacity);
  }
  return TRUE;
}

short push_to_array(struct dynamic_array *a, int num){
    if(!(a->size < a->capacity)){
      if(DEBUG){
        printf("Need to expand memory for push..\n");
      }
      if(!expand_dynamic_array(a)){
        if(DEBUG){
          printf("Memory expansion failed :/\n");
        }
        return FALSE;
      }
      if(DEBUG){
        printf("Memory expansion successful :)\n");
      }
    }
    a->data[a->size++] = num;
    return TRUE;
}

int main(int argc, char const *argv[]) {
  struct dynamic_array *fibs;
  fibs = malloc(sizeof(struct dynamic_array));
  if(!init_dynamic_array(fibs)){
    printf("%s\n", "Memory allocation problem, aborting process");
    return 1;
  }
  push_to_array(fibs,0);
  push_to_array(fibs,1);
  long sum = 0;
  while(fibs->data[fibs->size - 1] < 4000000){
    if(fibs->data[fibs->size - 1] % 2 == 0){
      sum += fibs->data[fibs->size - 1];
    }
    if(!push_to_array(fibs,fibs->data[fibs->size - 2] + fibs->data[fibs->size - 1])){
      printf("Could not push element onto array, aborting process\n");
      return 1;
    }
  }

  printf("Final Sum: %d\n", sum);

  return 0;
}
