    #!/bin/bash
    # Este script utiliza el comando escputil para comprobar su impresora
    echo "************************************************************"
    while true
    do
    echo "[1] Limpiar cabezal de impresión."
    echo "[2] Imprimir patrón de prueba."
    echo "[3] Nivel de tinta."
    echo "[4] Alinear cabezales.¡CUIDADO! Vea la ayuda antes."
    echo "[5] Alinear cabezal color. ¡CUIDADO! Vea la ayuda antes."
    echo "[6] Recoger status de impresora"
    echo "[7] Consultar Marca y Modelo"
    echo "[8] Consultar Modelos disponibles"
    echo "[9] Ayuda y Licencia"
    echo "[0] Salir"
    read -p "Escriba una opción: " OPCION
    echo "### ### ### ### ### ### ### ### ### ### ### ### ### ### ###"
    case $OPCION in
    1) escputil -c -qr /dev/usblp0;;
    2) escputil -n -qr /dev/usblp0;;
    3) escputil -i -qr /dev/usblp0;;
    4) escputil -a -qr /dev/usblp0;;
    5) escputil -o -qr /dev/usblp0;;
    6) escputil -s -qr /dev/usblp0;;
    7) escputil -d -qr /dev/usblp0;;
    8) escputil -M -qr /dev/usblp0 | more;;
    9) escputil -h -qr /dev/usblp0 | more; escputil -l -r /dev/usblp0;;
    0) echo "¡Que pase buen día…!"
    break;;
    *)
    echo "Opción no válida, pruebe otra vez.";;
    esac
    done
    exit 0 
