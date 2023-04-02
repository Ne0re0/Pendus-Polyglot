#!/bin/bash

function banniere() {
    echo "$(tput setaf 3)  ___      __________               .__        ___     
 / _ \_/\  \______   \_____    _____|  |__    / _ \_/\ 
 \/ \___/   |    |  _/\__  \  /  ___/  |  \   \/ \___/ 
            |    |   \ / __ \_\___ \|   Y  \           
            |______  /(____  /____  >___|  /           
                   \/      \/     \/     \/  $(tput setaf 7)"
}

function remplacer(){
    valide=0
    for (( i=0 ; i<$taille ; i++ )) 
        do 
            if [[ ${motClair:$i:1} == ${1:0:1} ]];then
                motCache[i]=${1:0:1}
            fi
        done
}

clear
banniere

numLigne=$(( RANDOM % 834 + 1 ))
motClair=$(sed "${numLigne}q;d" dictionnaire.txt)

taille=$(echo -n $motClair | wc -m)

motCache=()
for (( i=0 ; i<$taille ; i++ ))
    do 
        motCache[i]="_"
    done


nbErreurs=0
for (( ; ; ))
    do
        clear
        banniere
        echo ${motCache[@]}
        echo
        echo "Il vous reste $((9 - $nbErreurs)) erreur(s) possibles"
        echo -n "Saisissez une lettre : "
        read lettre
        while [[ ${#lettre} != 1 ]]
            do
                echo "Lettre non valide"
                echo -n "Saisissez une autre lettre : "
                read lettre
            done
        oldMotCache=${motCache[@]}
        remplacer $lettre
        if [[ ${motCache[@]} == ${oldMotCache[@]} ]]; then
            nbErreurs=$(($nbErreurs + 1))
        fi
        echo $nbErreurs
        if echo ${motCache[@]} | grep -q "_" ; then
            echo > /dev/null
        else
            break
        fi

        
        if [[ $nbErreurs == 9 ]]; then
            break
        fi
    done

clear
banniere
echo ${motCache[@]}

if echo ${motCache[@]} | grep -q "_" ; then
    echo "$(tput setaf 1)Dommage ! Le mot était ${motClair[@]}"
else
    echo "$(tput setaf 2)Bravo ! Le mot était ${motClair[@]}"
fi


