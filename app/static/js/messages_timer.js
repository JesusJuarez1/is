
// Función para cerrar el mensaje después de cierto tiempo con fade
function autoDismissMessage(messageId, showDuration, fadeDuration) {
  var message = document.getElementById(messageId);
  if (message) {
    // Mostrar el mensaje durante el tiempo especificado (en milisegundos)
    setTimeout(function () {
      message.style.opacity = 1;
    }, showDuration);

    // Desvanecer el mensaje de manera limpia
    setTimeout(function () {
      var opacity = 1;
      var fadeEffect = setInterval(function () {
        if (opacity > 0) {
          message.style.opacity = opacity.toFixed(1);
          opacity -= 0.1;
        } else {
          clearInterval(fadeEffect);
          message.style.display = 'none';
        }
      }, fadeDuration / 800);
    }, showDuration);
  }
}

// Llama a la función para cerrar automáticamente el mensaje de error
var errorMessage = document.getElementById('error-message');
var successMessage = document.getElementById('success-message');

if (errorMessage || successMessage) {
  var autoDismissDuration = errorMessage ? errorMessage.getAttribute('data-auto-dismiss') : successMessage.getAttribute('data-auto-dismiss');
  var showDuration = 8000; // Duración en milisegundos antes de comenzar el desvanecimiento (2 segundos)
  var fadeDuration = parseInt(autoDismissDuration) - showDuration; // Duración en milisegundos del desvanecimiento
  
  if (autoDismissDuration) {
    if (errorMessage) {
      autoDismissMessage('error-message', showDuration, fadeDuration);
    }
    
    if (successMessage) {
      autoDismissMessage('success-message', showDuration, fadeDuration);
    }
  }
}

  
  
