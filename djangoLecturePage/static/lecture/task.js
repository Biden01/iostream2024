// Предполагается, что у вас есть несколько фреймов с классом 'frame'
var frames = document.querySelectorAll('iframe'); // или другой селектор для ваших фреймов
var loadedFramesCount = 0;

function onFrameLoad() {
    loadedFramesCount++;
    if (loadedFramesCount === frames.length) {
        // Прокрутка наверх, когда все фреймы загружены
        window.scrollTo(0, 0);
    }
}

frames.forEach(function(frame) {
    frame.addEventListener('load', onFrameLoad);
});
