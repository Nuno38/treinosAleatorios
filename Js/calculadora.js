 
function criaCalculadora() {
  return {
    display: document.querySelector('.display'),
  
    inicia(){
      this.cliqueBotoes();
      this.pressEnter();
      
    },

    pressEnter(){
        this.display.addEventListener('keyup', e=>{
          if (e.keyCode===13){
            this.mathMake();
          }
        });
    },

    clearDisplay(){
       this.display.value='';
    },
    
     delOne(){
        this.display.value = this.display.value.slice(0,-1);
     },

     mathMake(){
         let math = this.display.value;

         try{
           math=eval(math);

           if(!math){
            alert('Conta inválida');
            return;
           }
           this.display.value=String (math);
         }catch(e){
             alert("Conta inválida");
             return;
         }
     },

    cliqueBotoes() {
      document.addEventListener('click', function (e) {
        const el = e.target;
        let letra ="C";

        if (el.classList.contains('btn-num')) {
          this.btnParaDisplay(el.innerText);
          
        }
          if(el.classList.contains('btn-clear')){
            this.clearDisplay();
          }
            
          if(el.classList.contains('btn-del')){
            this.delOne();
          }
          if(el.classList.contains("btn-eq")){
              this.mathMake();
          }

      }.bind(this));
    },
    btnParaDisplay(valor){
      this.display.value += valor;
    }
  };
}


const calculadora = criaCalculadora();
calculadora.inicia();
