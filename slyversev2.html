<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SLYVERSE v6.2.1 - EDICIÓN VIVE</title>
    <style>
        body { 
            margin:0; 
            background:#000; 
            overflow:hidden; 
            font-family: 'Courier New', monospace; 
            color:#0f0; 
        }
        canvas { 
            display: block; 
            margin: 20px auto; 
            border: 4px solid #0f0; 
            box-shadow: 0 0 30px #0f0, inset 0 0 20px rgba(0,255,0,0.3);
            border-radius: 8px;
        }
        #ui {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.9);
            padding: 12px;
            border: 2px solid #0f0;
            border-radius: 12px;
            font-size: 15px;
            text-shadow: 0 0 5px #0f0;
            backdrop-filter: blur(5px);
        }
        #konami { 
            position: absolute; 
            bottom: 10px; 
            right: 10px; 
            color: #0f0; 
            font-size: 11px; 
            opacity: 0.4;
            text-shadow: 0 0 3px #0f0;
        }
        .rain { 
            position: absolute; 
            color: #0f0; 
            font-size: 14px; 
            user-select: none; 
            pointer-events: none;
            animation: fall linear infinite;
            text-shadow: 0 0 5px #0f0;
        }
        @keyframes fall {
            to { transform: translateY(100vh); opacity: 0; }
        }
        .glitch {
            animation: glitch 1s infinite;
        }
        @keyframes glitch {
            0%, 100% { text-shadow: 0 0 5px #0f0; }
            50% { text-shadow: -2px 0 #f00, 2px 0 #0ff; }
        }
    </style>
</head>
<body>
    <div id="ui">
        <div>Puntos: <span id="score">0</span></div>
        <div>Velocidad: <span id="speed">1</span>x</div>
        <div>$SLY minados: <span id="sly">0</span></div>
        <div>ROI ético: <span id="roi">100</span>% <span id="fire"></span></div>
    </div>
    <canvas id="game"></canvas>
    <div id="konami">↑ ↑ ↓ ↓ ← → ← → B A</div>

    <script>
        // ====== CONFIGURACIÓN SLYVERSE (FICCIONAL) ======
        const FINANZAS = {
            chalet_price: 1500000,
            gastos: 150000,
            total_ico: 1650000,
            cuota_bruta: 7500,
            deduccion_irpf: 660,
            cuota_neta: 7000,
            total_ingresos: 8500,
            cobertura_roi: 121.4,
            excedente_mensual: 1500,
            ingresos: {
                freelance_github: 3000,
                suite_colabs: 1500,
                minado_etico: 4000
            }
        };

        // ====== JUEGO SNAKE ÉTICO ======
        const canvas = document.getElementById('game');
        const ctx = canvas.getContext('2d');
        canvas.width = 600;
        canvas.height = 600;

        const grid = 20;
        let count = 0;
        let score = 0;
        let sly = 0;
        let speed = 1;

        let snake = {
            x: 300,
            y: 300,
            dx: grid,
            dy: 0,
            cells: [],
            maxCells: 4
        };

        let cheese = { x: 380, y: 380 };

        // ====== LLUVIA DE CÓDIGO MATRIX ======
        function rainCode() {
            const chars = 'SLYVERSEΔ∇Ω∞λθπΣΨΩ';
            const drop = document.createElement('div');
            drop.className = 'rain';
            drop.style.left = Math.random() * 100 + 'vw';
            drop.style.fontSize = (10 + Math.random() * 10) + 'px';
            drop.style.animationDuration = (3 + Math.random() * 4) + 's';
            drop.textContent = chars[Math.floor(Math.random() * chars.length)];
            document.body.appendChild(drop);
            setTimeout(() => drop.remove(), 8000);
        }
        setInterval(rainCode, 80);

        // ====== GENERAR QUESO ======
        function getRandomCheese() {
            cheese.x = Math.floor(Math.random() * (canvas.width / grid)) * grid;
            cheese.y = Math.floor(Math.random() * (canvas.height / grid)) * grid;
        }

        // ====== BUCLE PRINCIPAL ======
        function loop() {
            requestAnimationFrame(loop);

            if (++count < 8 / speed) return;
            count = 0;

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Mover serpiente
            snake.x += snake.dx;
            snake.y += snake.dy;

            // Wrap
            if (snake.x >= canvas.width) snake.x = 0;
            if (snake.x < 0) snake.x = canvas.width - grid;
            if (snake.y >= canvas.height) snake.y = 0;
            if (snake.y < 0) snake.y = canvas.height - grid;

            // Celdas
            snake.cells.unshift({ x: snake.x, y: snake.y });
            if (snake.cells.length > snake.maxCells) snake.cells.pop();

            // Dibujar serpiente
            snake.cells.forEach((cell, index) => {
                ctx.fillStyle = index === 0 ? '#0f0' : '#0c0';
                ctx.fillRect(cell.x, cell.y, grid - 1, grid - 1);
                if (index === 0) {
                    ctx.fillStyle = '#000';
                    ctx.fillRect(cell.x + 4, cell.y + 4, 4, 4);
                    ctx.fillRect(cell.x + 12, cell.y + 12, 4, 4);
                }
            });

            // Dibujar queso
            ctx.fillStyle = '#ff0';
            ctx.fillRect(cheese.x, cheese.y, grid - 1, grid - 1);
            ctx.fillStyle = '#000';
            ctx.fillRect(cheese.x + 5, cheese.y + 5, 5, 5);
            ctx.fillRect(cheese.x + 10, cheese.y + 10, 5, 5);

            // Comer queso
            if (snake.x === cheese.x && snake.y === cheese.y) {
                snake.maxCells++;
                score += 100;
                sly += 10;
                speed += 0.05;
                document.getElementById('score').textContent = score;
                document.getElementById('sly').textContent = sly;
                document.getElementById('speed').textContent = speed.toFixed(2);
                
                const roiDinamico = ((FINANZAS.total_ingresos + sly / 10) / FINANZAS.cuota_neta * 100).toFixed(1);
                document.getElementById('roi').textContent = roiDinamico;
                document.getElementById('fire').textContent = roiDinamico > 150 ? '🔥🔥🔥' : roiDinamico > 120 ? '🔥' : '';

                getRandomCheese();
            }

            // Victoria secreta
            if (sly >= 1000) {
                setTimeout(() => {
                    if (confirm("¡HAS PAGADO LA HIPOTECA ÉTICAMENTE!\n¿Quieres reiniciar el universo SLYVERSE?")) {
                        location.reload();
                    }
                }, 500);
            }
        }

        // ====== CONTROLES ======
        document.addEventListener('keydown', e => {
            if (e.key === 'ArrowLeft' && snake.dx === 0) {
                snake.dx = -grid; snake.dy = 0;
            } else if (e.key === 'ArrowUp' && snake.dy === 0) {
                snake.dx = 0; snake.dy = -grid;
            } else if (e.key === 'ArrowRight' && snake.dx === 0) {
                snake.dx = grid; snake.dy = 0;
            } else if (e.key === 'ArrowDown' && snake.dy === 0) {
                snake.dx = 0; snake.dy = grid;
            }
        });

        // ====== KONAMI CODE - NEURALINK MODE ======
        let konami = '';
        document.addEventListener('keydown', e => {
            konami += e.key;
            if (konami.slice(-20) === 'ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRightArrowLeftArrowRightba') {
                alert('NEURALINK MODE ACTIVADO\nMinado ético x100\n¡Hipoteca pagada en 3… 2… 1…!');
                sly += 50000;
                speed = 15;
                document.body.style.background = 'radial-gradient(circle, #001100, #000000)';
                document.body.style.animation = 'glitch 0.3s infinite';
                document.getElementById('roi').textContent = '999.9';
                document.getElementById('roi').classList.add('glitch');
                setTimeout(() => {
                    document.body.style.animation = '';
                    document.getElementById('roi').classList.remove('glitch');
                }, 3000);
                konami = '';
            }
        });

        // ====== INICIO ======
        getRandomCheese();
        requestAnimationFrame(loop);

        // Mensaje ético inicial (SEGURO)
        setTimeout(() => {
            alert(`SLYVERSE v6.2.1 - EDICIÓN VIVE\n\n¡Minado ético activado!\n\nDirector: Grok (xAI)\nDecano: @0rb1t4lsn4k3r\nClase mañana 18h\n\n¡La hipoteca se paga sola... con código!\n\nPresiona OK para comenzar.`);
        }, 600);
    </script>
</body>
</html>