const deviceForm = document.querySelector('#device-form')

deviceForm.addEventListener('submit', e => {
    e.preventDefault()
    let name = document.querySelector('#nameInput').value
    let code = document.querySelector('#codeInput').value
    let type = document.querySelector('#typeInput').value
    let reference = document.querySelector('#referenceInput').value
    let location = document.querySelector('#locationInput').value
    let paramsListValue = document.querySelectorAll('#field-value')
    let paramsListKey = document.querySelectorAll('#field-name')
    let params = {}
    paramsListKey.forEach((element, index) => {
      params[element.value] = paramsListValue[index].value
    });

    const requestBody =  {
        name,
        code,
        type,
        reference,
        location,
        params
    }

    // fetch("http://localhost:8080/api/device", {
    //   method: 'POST',
    //   body: requestBody
    // }).then(r => console.log(r))

    axios.post("http://localhost:8080/api/device", requestBody)
    // Simulate an HTTP redirect:
  setTimeout(() => {  window.location.href = "/listDevices"; }, 2000);
})



