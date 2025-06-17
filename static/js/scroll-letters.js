document.addEventListener("DOMContentLoaded", () => {
  const letters = document.querySelectorAll('.letter');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const trigger = window.innerHeight / 2;

    letters.forEach((letter, i) => {
      const delay = i * 50;
      const appearAt = trigger + delay;

      if (scrollY >= appearAt) {
        letter.style.opacity = '1';
        letter.style.transform = 'translateY(0) scale(1)';
      } else {
        letter.style.opacity = '0';
        letter.style.transform = 'translateY(-200px) scale(0.5)';
      }
    });
  });
});
