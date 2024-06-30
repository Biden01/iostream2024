// // Предполагается, что у вас есть несколько фреймов с классом 'frame'
// var frames = document.querySelectorAll('iframe'); // или другой селектор для ваших фреймов
// var loadedFramesCount = 0;
//
// function onFrameLoad() {
//     loadedFramesCount++;
//     if (loadedFramesCount === frames.length) {
//         // Прокрутка наверх, когда все фреймы загружены
//         window.scrollTo(0, 0);
//     }
// }

// frames.forEach(function(frame) {
//     frame.addEventListener('load', onFrameLoad);
// });

document.addEventListener('DOMContentLoaded', () => {
    const players = Array.from(document.querySelectorAll('video, audio')).map(p => new Plyr(p));
});

window.onload = function () {
    // Предположим, что у всех ссылок на видео есть класс 'video-link'
    var videoLinks = document.querySelectorAll("source");

    videoLinks.forEach(function (link) {
        link.remove();
    });
};


var code;

$(function() {
    code = ace.edit("editor");                      // создаем редактор из элемента с id="code"
    code.getSession().setMode("ace/mode/python");   // говорим что код надо подсвечивать как Python код
    code.getSession().setUseWorker(true);
    code.setHighlightActiveLine(true); // Включите подсветку активной строки
    code.setShowPrintMargin(true);               // опционально: убираем вертикальную границу в 80 сиволов
    code.setOptions({
    maxLines: Infinity,                       // опционально: масштабировать редактор вертикально по размеру кода
    fontSize: "12pt",                         // опционально: размер шрифта ставим побольше
});
    code.$blockScrolling = Infinity;              // отключаем устаревшие, не поддерживаемые фишки редактора
});

// function main() {
//     let code_text = code.getValue();
//     console.log(code_text);
// }
//
// function runit() {
//     var prog = code.getValue();
//     var mypre = document.getElementById("output");
//     Sk.configure({
//         output: function (text) {
//             mypre.innerHTML += text;
//         },
//         read: function (x) {
//             if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
//                 throw "File not found: '" + x + "'";
//             return Sk.builtinFiles["files"][x];
//         }
//     });
//     Sk.misceval.asyncToPromise(function () {
//         return Sk.importMainWithBody("<stdin>", false, prog, true);
//     });
// }