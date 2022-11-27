<h1>Wordle Game Project</h1>

<p>La finalizarea acestui proiect au participat urmatorii:</p>
<ul>
    <li style = "list-style-type: circle;" ><Ocnaru Mihai Octavian, Grupa 131</li>
    <li style = "list-style-type: circle;" >Caracas Radu Nicolae, Grupa 131</li>
    <li style = "list-style-type: circle;" >Pistol Tudor, Grupa 131</li>
    <li style = "list-style-type: circle;" >Iordache Andrei Tudor, Grupa 131</li>
</ul>

<h1>Scurta descriere</h1>

<p>    Proiectul nostru este realizat in intregime in limbajul PYTHON. Am incercat o implementare
    in C/C++ dar am realizat ca in python cu cateva optimizari putem sa ajungem la rezultatele dorite 
    mai repede.
        Avem programul principal, denumit #gui# care instantiaza atat interfata grafica pentru joc cat si 2 
    subprocese, unul pentru guess-urile programului care joaca wordle optim si cel de-al doilea pentru 
    interfata propriu zisa.
    Programele comunica printr-un fisier, guess-urile fiind validate prin pattern-ul de culori si trimise inapoi la 
    pentru un nou guess. 

    Note - Pentru mac, culorile din modulul tkinter din python nu functioneza.
    De asemenea butonul 'Again' genereaza noi ferestre fara a le inchide pe cele vechi.
    Pentru o experienta cat mai buna recomandam windows :)
</p>


<h2>Eficienta si reduntanta programului</h2>

<p>Numarul mediu de incercari pe care programul le are <em>afererent listei propuse</em> este de 4.37 incercari/cuvant</p>

![WhatsApp Image 2022-11-27 at 3 20 40 PM](https://user-images.githubusercontent.com/84620187/204138403-2594a39a-847c-4205-b336-2ed09bbd823e.jpeg)

<h2>Cum sa rulezi programele</h2>

<ol>

<li style="list-style-type:armenian;">Git clone la repositoriul de la adresa asta: <a>https://github.com/w-i-l/ASM-Project</a></li>
<li>Se ruleaza in terminal comenzile de mai jos</li>
 
    
    git clone https://github.com/w-i-l/ASM-Project
    cd ASM-Project
    cd Wordle
    python class_gui.py
    
<li style="list-style-type:armenian;">Enjoy the visuals :)</li>
    
   
    
</ol>