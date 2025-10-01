document.addEventListener("DOMContentLoaded", function() {
  const cpfInput = document.getElementById("id_cpf");

  cpfInput.addEventListener("input", function(e) {
    let value = e.target.value;

    // Remove tudo que não for número
    value = value.replace(/\D/g, "");

    // Aplica a máscara: 000.000.000-00
    if (value.length > 3 && value.length <= 6)
      value = value.replace(/(\d{3})(\d+)/, "$1.$2");
    else if (value.length > 6 && value.length <= 9)
      value = value.replace(/(\d{3})(\d{3})(\d+)/, "$1.$2.$3");
    else if (value.length > 9)
      value = value.replace(/(\d{3})(\d{3})(\d{3})(\d+)/, "$1.$2.$3-$4");

    // Atualiza o campo formatado
    e.target.value = value;
  });
});