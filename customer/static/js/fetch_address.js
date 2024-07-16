document.addEventListener('DOMContentLoaded', function () {
  const zipCodeField = document.getElementById('id_zip_code');
  const neighborhoodField = document.getElementById('id_neighborhood');
  const streetField = document.getElementById('id_street');

  zipCodeField.addEventListener('change', function () {
      const zipCode = zipCodeField.value.replace(/\D/g, '');

      if (zipCode.length === 8) {
          fetch(`https://viacep.com.br/ws/${zipCode}/json/`)
              .then(response => {
                  if (response.status === 200) {
                      return response.json();
                  } else {
                      throw new Error('CEP inválido');
                  }
              })
              .then(data => {
                  if (!data.erro) {
                      neighborhoodField.value = data.bairro;
                      streetField.value = data.logradouro;
                  } else {
                      neighborhoodField.value = '';
                      streetField.value = '';
                      alert('CEP não encontrado');
                  }
              })
              .catch(error => {
                  console.error('Erro ao buscar o endereço:', error);
                  neighborhoodField.value = '';
                  streetField.value = '';
              });
      } else {
          neighborhoodField.value = '';
          streetField.value = '';
      }
  });
});
