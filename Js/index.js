/*
function formataData(num) {
    return num >= 10 ? num : `0${num}`;
}

function dataFormatada(data) {
    const dia = formataData(data.getDate());
    const mes = formataData(data.getMonth() + 1);
    const ano = formataData(data.getFullYear());
    const horas = formataData(data.getHours());
    const second = formataData(data.getMinutes());
    const diaDaSemana = formataData(data.getDay());

    let domingo = `Domingo`;
    let segunda = `Segunda`;
    let ter = `Terça`;
    let quar = `Quarta`;
    let quinta = `Quinta`;
    let sexta = `Sexta`;
    let sab = `Sábado`;

    if (diaDaSemana == 0) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${domingo}`;

    } else if (diaDaSemana == 1) {

        return `${dia}/${mes}/${ano} ${horas}:${second} ${segunda}`;

    } else if (diaDaSemana == 2) {

        return `${dia}/${mes}/${ano} ${horas}:${second} ${ter}`;

    } else if (diaDaSemana == 3) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${quar}`;

    } else if (diaDaSemana == 4) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${quinta}`;

    } else if (diaDaSemana == 5) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${sexta}`;

    } else if (diaDaSemana == 6) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${sab}`;
    }
}

const data = new Date();
let dataBrasil = dataFormatada(data);
console.log(dataBrasil);
*/

//------- exercicio 
/*
function formataData(num) {
    return num >= 10 ? num : `0${num}`;
}

function dataFormatada(data) {
    const dia = formataData(data.getDate());
    const mes = formataData(data.getMonth() + 1);
    const ano = formataData(data.getFullYear());
    const horas = formataData(data.getHours());
    const second = formataData(data.getMinutes());
    const diaDaSemana = formataData(data.getDay());

    let dias = ["domingo", "segunda", "terça", "Quarta", "Quinta", "Sexta", "Sabádo"];
   

    if (diaDaSemana == 0) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${dias[0]}`;

    } else if (diaDaSemana == 1) {

        return `${dia}/${mes}/${ano} ${horas}:${second} ${dias[1]}`;

    } else if (diaDaSemana == 2) {

        return `${dia}/${mes}/${ano} ${horas}:${second} ${dias[2]}`;

    } else if (diaDaSemana == 3) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${dias[3]}`;

    } else if (diaDaSemana == 4) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${dias[4]}`;

    } else if (diaDaSemana == 5) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${dias[5]}`;

    } else if (diaDaSemana == 6) {

        return `${dia}/${mes}/${ano} ${horas}:${second}  ${dias[6]}`;
    }
}

const data = new Date();
let dataBrasil = dataFormatada(data);

const div = document.querySelector('#horas');
div.innerHTML= dataBrasil;
*/

// exercicios de lista
/*
const paragrafos = document.querySelector('.paragrafos');
const ps = paragrafos.querySelectorAll('p');

const estilosColorBody = estilos.body.backgroundColor;
console.log (estilosColorBody);


for(let p of ps){
p.style.estilosColorBody = backgroundColor;
p.style.color = '#fffff';
}
*/

/*
function random (min,max){
    const r = Math.random () *(max - min) + min;
    return Math.floor(r);
}

const min = 1;
const max = 50;

do {
    rand = random(min, max);
    console.log(rand)
}while(rand !=10);
*/

/* uso de ternario--
function maiorNumero(numero1, numero2) {
    return numero1 > numero2 ? numero1:numero1;
    
}

const maiorNumero2= (numero1,numero2) => numero1 > numero2 ? numero1 : numero2;
 console.log(maiorNumero2(10,20));
 

 const telaModoPaisagem = (largura, altura) => largura > altura;
 console.log(telaModoPaisagem(1920, 1080));
 */

//exercicio
/*
let number =3;
function verifica(){
  if(number/3 ==0){
   console.log("é divisivel por 3");
  }else if (number/5==0){
     console.log("é divisivel po 5")
  }else if(number/3==0 & number/5==0 ){
   console.log("é divisivel por 3 e 5");
  }
  else{
   console.log("não é divisivém por 3 ou 5");
  }
}

verifica();
*/

// Timer online
/*
function getTimeSeconds(segundos) {
    let data = new Date(segundos * 1000);
    return data.toLocaleTimeString('pt-BR', {
        hour12: false,
        timeZone: 'UTC'
    });
}

const relogio = document.querySelector('.relogio');
let segundos = 0;
let timer;

function iniciaRelogio() {

    timer = setInterval(function () {
        segundos++;
        relogio.innerHTML = getTimeSeconds(segundos);
    }, 1000)

}

document.addEventListener('click', function (selection) {
    const select = selection.target;

    if (select.classList.contains('iniciar')) {
        relogio.classList.remove('stop');
        clearInterval(timer);
        iniciaRelogio();
    }

    if (select.classList.contains('reset')) {
        segundos = 0;
        clearInterval(timer);
        relogio.innerHTML = '00:00:00';
        relogio.classList.remove('stop');
    }

    if (select.classList.contains('pausar')) {
        relogio.classList.add('stop');
        clearInterval(timer);
    }
});  

//timer
*/

// Lista de tarefas que deleta e inclui algo

const inputTarefas = document.querySelector('.new-tarefas');
const btnTarefa = document.querySelector('.btn-tarefa');
const tarefa = document.querySelector('.tarefas');


inputTarefas.addEventListener('keypress',function(e){
    if (e.keyCode === 13){
        
        if (!inputTarefas.value) return;
        criaTarefa(inputTarefas.value);
    }

});

function limpaImput(){
    inputTarefas.value = '';
    inputTarefas.focus();
}

btnTarefa.addEventListener('click', function(clicou){
     clicou = btnTarefa;
    if (!inputTarefas.value) return;
    console.log(inputTarefas.value);
    criaTarefa(inputTarefas.value);

});

function criaTarefa(textoInput) {
    const li = criaLi();
    li.innerText = textoInput;
    tarefa.appendChild(li);
    limpaImput();
    criaBotaoApagar(li);
    salvarTarefa();
}

function criaLi() {
    const li = document.createElement('li');
    return li;
}

function criaBotaoApagar(li){
    li.innerText += '    '+'  '+ '   ';
   const botaoApagar = document.createElement('button');
   botaoApagar.innerText = 'Apagar';
   botaoApagar.setAttribute('class','apagar');
   li.appendChild(botaoApagar);
}


document.addEventListener('click', function(e){
    const el =e.target;
    if(el.classList.contains('apagar')){
        el.parentElement.remove();
        salvarTarefa();
    }
});

function salvarTarefa(){
    const liTarefas = tarefa.querySelectorAll('li');
    const listaDeTarefas = [];

    for (let tarefas of liTarefas){

        let tarefaTexto = tarefas.innerText;
        tarefaTexto = tarefaTexto.replace('Apagar', ''). trim();
        listaDeTarefas.push(tarefaTexto);
        
}
const tarefasJSON = JSON.stringify(listaDeTarefas);
localStorage.setItem('tarefas',tarefasJSON);

}

function adicionaTarefasSalvas(){
    const tarefas = localStorage.getItem('tarefas');
    const listaDeTarefas = JSON.parse(tarefas);
    
    for (let tarefaa of listaDeTarefas){
        criaTarefa(tarefaa);
    }
}

adicionaTarefasSalvas();