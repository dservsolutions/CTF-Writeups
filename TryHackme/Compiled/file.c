undefined8 main(void)

{
  int Comparistion_diff;
  char password [32];
  
  fwrite("Password: ",1,10,stdout);
  __isoc99_scanf("DoYouEven%sCTF",password);
  Comparistion_diff = strcmp(password,"__dso_handle");
  if ((-1 < Comparistion_diff) &&
     (Comparistion_diff = strcmp(password,"__dso_handle"), Comparistion_diff < 1)) {
    printf("Try again!");
    return 0;
  }
  Comparistion_diff = strcmp(password,"_init");
  if (Comparistion_diff == 0) {
    printf("Correct!");
  }
  else {
    printf("Try again!");
  }
  return 0;
}