// static/js/inputmask_config.js
document.addEventListener('DOMContentLoaded', function() {
  // Aplicando máscara para CPF e CNPJ
  document.getElementById('id_cnpj').addEventListener('input', function() {
      var value = this.value.replace(/\D/g, '');
      this.value = value.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
      
  });

  document.getElementById('id_contact').addEventListener('input', function(e) {
    var value = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos
    var formattedValue = '';

    if (value.length > 0) {
        formattedValue = '(' + value.substring(0, 2); // Adiciona parêntese de abertura e os primeiros 2 dígitos
    }
    if (value.length > 2) {
        formattedValue += ') ';

        if (value.length <= 10) {
            formattedValue += value.substring(2, 6); // Adiciona os próximos 4 dígitos (caso de 10 dígitos)
        } else {
            formattedValue += value.substring(2, 7); // Adiciona os próximos 5 dígitos (caso de 11 dígitos)
        }
    }
    if (value.length > 6) {
        if (value.length <= 10) {
            formattedValue += '-' + value.substring(6, 10); // Adiciona traço e os últimos 4 dígitos (caso de 10 dígitos)
        } else {
            formattedValue += '-' + value.substring(7, 11); // Adiciona traço e os últimos 4 dígitos (caso de 11 dígitos)
        }
    }

    this.value = formattedValue.trim(); // Atualiza o valor do campo, removendo espaços extras
  });



  // Aplicando máscara para CEP
  document.getElementById('id_zip_code').addEventListener('input', function() {
    var value = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos

    if (value.length > 5) {
        this.value = value.substring(0, 5) + '-' + value.substring(5, 8); // Formatação do CEP
    } else {
        this.value = value; // Mantém o valor sem formatação se não houver 8 dígitos
    }
  });
});
