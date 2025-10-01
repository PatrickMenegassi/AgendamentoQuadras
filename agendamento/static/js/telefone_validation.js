document.addEventListener("DOMContentLoaded", function() {
  const telefoneInput = document.getElementById("id_telefone");

  telefoneInput.addEventListener("input", function(e) {
    let value = e.target.value;

    // Remove tudo que não for número
    value = value.replace(/\D/g, "");

    value = value.replace(/\D/g,'')
    value = value.replace(/(\d{2})(\d)/,"($1) $2")
    value = value.replace(/(\d)(\d{4})$/,"$1-$2")

    // Atualiza o campo formatado
    e.target.value = value;
  });
});