document.getElementById('myform').addEventListener('submit', function(event){
  event.preventDefault();

  const num = document.getElementById('numero').value;
  const nom = document.getElementById('nombre').value;
  const loc = document.getElementById('localidad').value;

   if (num === "" || nom === "" || loc ==='') {
        alert('Por favor, rellene todos los campos.');
   }else {
        event.currentTarget.submit();
   }
  });