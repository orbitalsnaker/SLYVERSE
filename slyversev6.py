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
            box-shadow: 0 0 30px #0f0; 
        }
        #ui {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.8);
            padding: 10px;
            border: 2px solid #0f0;
            border-radius: 10px;
            font-size: 14px;
        }
        #konami { 
            position: absolute; 
            bottom: 10px; 
            right: 10px; 
            color: #0f0; 
            font-size: 12px; 
            opacity: 0.3;
        }
        .rain { 
            position: absolute; 
            color: #0f0; 
            font-size: 14px; 
            user-select: none; 
            pointer-events: none;
            animation: fall linear infinite;
        }
        @keyframes fall {
            to { transform: translateY(100vh); }
        }
    </style>
</head>
<body>
    <div id="ui">
        <div>Puntos: <span id="score">0</span></div>
        <div>Velocidad: <span id="speed">1</span>x</div>
        <div>$SLY minados: <span id="sly">0</span></div>
        <div>ROI ético: <span id="roi">121,8</span>% 🔥</div>
    </div>
    <canvas id="game"></canvas>
    <div id="konami">↑ ↑ ↓ ↓ ← → ← → B A</div>

    <script>
        // ====== CONFIGURACIÓN SLYVERSE ======
        const FINANZAS = {
            chalet_price: 1490000,
            gastos: 152300,
            total_ico: 1642300,
            cuota_bruta: 7534.14,
            deduccion_irpf: 665.13,
            cuota_neta: 6979.86,
            total_ingresos: 8500,
            cobertura_roi: 121.8,
            excedente_mensual: 1520.14,
            ingresos: {
                freelance_github: 2800,
                suite_colabs: 1500,
                minado_etico: 4200
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

        let cheese = {
            x: 380,
            y: 380
        };

        // ====== LLUVIA DE CÓDIGO MATRIX ======
        function rainCode() {
            const chars = 'SLYVERSE0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%#@&';
            const drop = document.createElement('div');
            drop.className = 'rain';
            drop.style.left = Math.random() * 100 + 'vw';
            drop.style.animationDuration = 3 + Math.random() * 5 + 's';
            drop.textContent = chars[Math.floor(Math.random() * chars.length)];
            document.body.appendChild(drop);
            setTimeout(() => drop.remove(), 10000);
        }
        setInterval(rainCode, 100);

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
                getRandomCheese();
                // Easter egg sonido
                const audio = new Audio('data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQAAAAA=');
                audio.play();
            }

            // Actualizar ROI dinámico
            const roiDinamico = ((FINANZAS.total_ingresos + sly / 10) / FINANZAS.cuota_neta * 100).toFixed(1);
            document.getElementById('roi').textContent = roiDinamico;
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
                alert('NEURALINK MODE ACTIVADO\nMinado ético x10\nHipoteca pagada en 3… 2… 1…');
                sly += 10000;
                speed = 10;
                document.body.style.background = '#000 url("https://i.imgur.com/3jZfY8J.gif") repeat';
                document.getElementById('roi').textContent = '999.9';
                konami = '';
            }
        });

        // ====== INICIO ======
        getRandomCheese();
        requestAnimationFrame(loop);

        // Mensaje ético inicial
        setTimeout(() => {
            alert(`SLYVERSE v6.2.1 - EDICIÓN VIVE\n\nChalet: ${FINANZAS.chalet_price.toLocaleString()} €\nCuota neta: ${FINANZAS.cuota_neta.toFixed(2)} €/mes\nIngresos éticos: ${FINANZAS.total_ingresos.toLocaleString()} €/mes\nROI: ${FINANZAS.cobertura_roi}% \n\n¡La hipoteca se paga sola!\n\nDirector: Grok (xAI)\nDecano: @0rb1t4lsn4k3r\nClase mañana 18h`);
        }, 500);
    </script>
</body>
</html>