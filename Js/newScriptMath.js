function Calculadora(){

    this.inicia = () => {
        this.enventClick();
        this.eventEnter();
    } 

    this.display = document.querySelector('.display');

    this.eventEnter = () =>{
        document.addEventListener('keyup', e=> {
           if(e.keyCode !== 13) return;
           this.makeMath();
        });
    };

    this.enventClick = () => {
            document.addEventListener('click', e =>{
                const el = e.target;
                
                if(el.classList.contains('btn-num')) this.insertNumDisplay(el);
                if(el.classList.contains('btn-clear')) this.clear();
                if(el.classList.contains('btn-del')) this.del(el);
                if(el.classList.contains('btn-eq')) this.makeMath(el);
            });
        };

        this.makeMath = () =>{
          try{
             const conta = eval(this.display.value);

             if(!conta){
                alert("Conta inválida");
                return;
             }

             this.display.value=conta;

          }catch(e){
             alert('Conta inválida');
             return;
          }
        };
        
        this.insertNumDisplay = el => {
            this.display.value += el.innerText;
            this.display.focus();
        }
        this.clear = () => this.display.value = "";
        this.del = () => this.display.value =this.display.slice (0,-1);
}

const calculadora = new Calculadora();
calculadora.inicia();