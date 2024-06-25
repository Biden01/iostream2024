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

let player

document.addEventListener('DOMContentLoaded', () => {
  const players = Array.from(document.querySelectorAll('video, audio')).map(p => new Plyr(p));
});

window.onload = function() {
    // Предположим, что у всех ссылок на видео есть класс 'video-link'
    var videoLinks = document.querySelectorAll("source");

    videoLinks.forEach(function(link) {
        link.remove();
    });
};

