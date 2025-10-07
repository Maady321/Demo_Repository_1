const canvas = document.getElementById('dna-canvas');
const ctx = canvas.getContext('2d');
const centerX = canvas.width / 2;
const centerY = canvas.height / 2;
const helixRadius = 70;
const helixHeight = 400;
const helixTurns = 2.5;
const dotCount = 32;
const baseColors = ["#01ffe3", "#88f964"];
let angle = 0;

function drawDna() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.save();
  ctx.globalAlpha = 0.22;
  ctx.strokeStyle = "#00faff";
  ctx.beginPath();
  for (let i = 0; i <= 1; i += 0.001) {
    const t = i * helixTurns * Math.PI * 2;
    const x = centerX + helixRadius * Math.sin(t + angle + Math.PI * i);
    const y = centerY + (i ? 1 : -1) * 10 + helixHeight * (i - i * i);
    ctx.lineTo(x, centerY + ((t / (helixTurns * Math.PI * 2)) - 0.5) * helixHeight);
  }
  ctx.stroke();
  ctx.restore();

  for (let i = 0; i < dotCount; i++) {
    const t = (i / (dotCount - 1)) * helixTurns * Math.PI * 2;
    const progression = (t / (Math.PI * 2 * helixTurns));
    const y = centerY + (progression - 0.5) * helixHeight;
    const x1 = centerX + helixRadius * Math.sin(t + angle);
    const x2 = centerX + helixRadius * Math.sin(t + angle + Math.PI);

    ctx.save();
    ctx.strokeStyle = "#44eeec88";
    ctx.globalAlpha = 0.5;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x1, y);
    ctx.lineTo(x2, y);
    ctx.stroke();
    ctx.restore();

    for (let k = 0; k < 2; k++) {
      const x = centerX + helixRadius * Math.sin(t + angle + Math.PI * k);
      ctx.save();
      ctx.beginPath();
      ctx.arc(x, y, 10, 0, Math.PI * 2);
      ctx.shadowColor = baseColors[k];
      ctx.shadowBlur = 22;
      ctx.fillStyle = baseColors[k];
      ctx.globalAlpha = 0.93;
      ctx.fill();
      ctx.restore();
    }
  }
  angle += 0.019;
  requestAnimationFrame(drawDna);
}
drawDna();
