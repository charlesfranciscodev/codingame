#include <iostream>

using namespace std;

int distanceEdit(const string& chaine1, const string& chaine2);

int main() {
  string chaine1;
  getline(cin, chaine1);
  string chaine2;
  getline(cin, chaine2);
  cout << distanceEdit(chaine1, chaine2) << endl;
}

int distanceEdit(const string& chaine1, const string& chaine2) {
  int taille1 = chaine1.length();
  int taille2 = chaine2.length();
  // tableau des sous-problèmes
  int cache[taille1];
  int index1, index2, distancePrec, distance, resultat;

  if (chaine1 == chaine2) {
    resultat = 0;
  } else if (taille1 == 0) {
    resultat = taille2;
  } else if (taille2 == 0) {
    resultat = taille1;
  } else {
    // pour une chaîne vide, tous les caractères doivent être insérés
    for (index1 = 0; index1 < taille1; ++index1)
      cache[index1] = index1 + 1;

    for (index2 = 0; index2 < taille2; ++index2) {
      char lettre2 = (char) tolower(chaine2[index2]);
      // si chaine1 est vide, il faut enlever tous les caractères de chaine2
      resultat = distancePrec = index2;
      for (index1 = 0; index1 < taille1; ++index1) {
        distance = lettre2 == (char) tolower(chaine1[index1]) ? distancePrec : distancePrec + 1;
        distancePrec = cache[index1];
        // trouver le minimum
        cache[index1] = resultat = distancePrec > resultat
          ? distance > resultat
            ? resultat + 1 // effacer
            : distance    // remplacer ou même lettre
          : distance > distancePrec
            ? distancePrec + 1 // insérer
            : distance;   // remplacer ou même lettre
      }
    }
  }

  return resultat;
}