'use strict';
function changeCamera(video, src, poster) {
  const time = video.currentTime;
  const playing = !video.paused;
  video.pause();
  video.src = src;
  video.poster = poster;
  video.load();
  video.addEventListener('loadedmetadata', () => {
    if (Number.isFinite(video.duration)) video.currentTime = Math.min(time, Math.max(0, video.duration - 0.1));
    if (playing) video.play().catch(() => {});
  }, { once: true });
}
document.querySelectorAll('.view-switch button').forEach(button => {
  button.addEventListener('click', () => {
    const group = button.closest('.view-switch');
    group.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    changeCamera(button.closest('.demo').querySelector('video'), button.dataset.src, button.dataset.poster);
  });
});
document.querySelectorAll('[data-camera]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('[data-camera]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    document.querySelectorAll('.sim-grid video').forEach(video => {
      const stem = video.dataset.stem + (button.dataset.camera === 'wrist' ? '-wrist' : '');
      // Keep all 25 clips lazy until the visitor plays a clip.
      video.pause(); video.removeAttribute('src');
      video.querySelector('source').src = `assets/${stem}.mp4`;
      video.poster = `assets/${stem}.jpg`; video.load();
    });
  });
});
document.getElementById('pause-demos').addEventListener('click', () => document.querySelectorAll('video').forEach(v => v.pause()));
const dialog = document.getElementById('video-dialog');
const largeVideo = dialog.querySelector('video');
document.querySelectorAll('.expand').forEach(button => {
  button.addEventListener('click', () => {
    const figure = button.closest('figure'); const video = figure.querySelector('video');
    video.pause();
    largeVideo.src = video.currentSrc || video.querySelector('source').src;
    largeVideo.poster = video.poster;
    dialog.querySelector('p').textContent = figure.querySelector('figcaption').textContent;
    dialog.showModal();
    largeVideo.play().catch(() => {});
  });
});
document.getElementById('close-video').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
dialog.addEventListener('close', () => { largeVideo.pause(); largeVideo.removeAttribute('src'); largeVideo.load(); });
// Pause offscreen clips so the galleries do not consume background resources.
const observer = new IntersectionObserver(entries => entries.forEach(entry => {
  if (!entry.isIntersecting) entry.target.pause();
}), { threshold: 0 });
document.querySelectorAll('main video').forEach(v => observer.observe(v));
