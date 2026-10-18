```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>LUCY PRO v3.0 - Asistente IA</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons CDN -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: #080a0f;
            color: #e2e8f0;
        }

        h1, h2, .font-heading {
            font-family: 'Space Grotesk', sans-serif;
        }

        /* Glassmorphism & Neon Effects */
        .glass-card {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(56, 189, 248, 0.15);
        }

        .glass-input {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(56, 189, 248, 0.25);
        }

        .pulse-cyan {
            box-shadow: 0 0 12px rgba(6, 182, 212, 0.6);
            animation: pulse-glow 2s infinite;
        }

        @keyframes pulse-glow {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(6, 182, 212, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(6, 182, 212, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(6, 182, 212, 0); }
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 5px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #1e293b;
            border-radius: 9999px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #334155;
        }
    </style>
</head>
<body class="h-[100dvh] flex flex-col justify-between overflow-hidden antialiased">

    <!-- CABECERA SUPERIOR / HEADER -->
    <header class="glass-card z-50 px-4 py-3 flex items-center justify-between border-b border-slate-800 shrink-0 shadow-lg shadow-black/40">
        <div class="flex items-center gap-3">
            <div class="relative">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-cyan-500 via-teal-500 to-indigo-500 flex items-center justify-center text-slate-950 font-bold shadow-lg shadow-cyan-500/25">
                    <i data-lucide="sparkles" class="w-5 h-5"></i>
                </div>
                <span id="status-indicator" class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 bg-emerald-400 rounded-full border-2 border-slate-950 pulse-cyan"></span>
            </div>
            <div>
                <h1 class="font-bold text-base text-slate-100 flex items-center gap-2 tracking-wide">
                    LUCY <span class="text-[10px] font-bold px-2 py-0.5 rounded-md bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">PRO v3.0</span>
                </h1>
                <p id="status-text" class="text-xs text-emerald-400 font-medium flex items-center gap-1">
                    <i data-lucide="wifi" class="w-3 h-3"></i> Red Global Activa
                </p>
            </div>
        </div>

        <!-- ACCIONES DE CONTROL Y MEMORIA -->
        <div class="flex items-center gap-1.5">
            <button onclick="limpiarChat()" title="Limpiar pantalla de chat" class="p-2.5 rounded-xl bg-slate-800/70 hover:bg-slate-700/70 text-slate-400 hover:text-cyan-300 transition-all border border-slate-700/50 active:scale-95">
                <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
            </button>
            <button onclick="reiniciarMemoria()" title="Vaciar almacenamiento en caché" class="p-2.5 rounded-xl bg-slate-800/70 hover:bg-slate-700/70 text-slate-400 hover:text-amber-400 transition-all border border-slate-700/50 active:scale-95">
                <i data-lucide="trash-2" class="w-4 h-4"></i>
            </button>
        </div>
    </header>

    <!-- ÁREA PRINCIPAL DE CHAT (SCROLLABLE) -->
    <main id="chat-container" class="flex-1 overflow-y-auto p-4 space-y-4 max-w-2xl w-full mx-auto">
        
        <!-- BIENVENIDA DE LUCY -->
        <div class="flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 shrink-0 mt-1 shadow-sm">
                <i data-lucide="bot" class="w-4 h-4"></i>
            </div>
            <div class="glass-card p-4 rounded-2xl rounded-tl-sm max-w-[88%] text-sm leading-relaxed space-y-3">
                <p class="font-semibold text-cyan-400 font-heading text-base">¡Hola! Soy Lucy PRO v3.0 🤖✨</p>
                <p class="text-slate-300">Puedo investigar cualquier tema en internet mediante síntesis inteligente o responder usando mi memoria local si te quedas sin conexión a datos.</p>
                
                <p class="text-xs text-slate-400 font-medium pt-1">Prueba con alguna sugerencia rápida:</p>
                <div class="flex flex-wrap gap-2">
                    <button onclick="usarSugerencia('¿Qué es la célula?')" class="text-xs bg-slate-800/80 hover:bg-cyan-500/20 text-slate-300 hover:text-cyan-300 px-3 py-1.5 rounded-xl border border-slate-700 hover:border-cyan-500/40 transition-all active:scale-95">
                        🔬 Concepto de Célula
                    </button>
                    <button onclick="usarSugerencia('Anatomía del corazón')" class="text-xs bg-slate-800/80 hover:bg-cyan-500/20 text-slate-300 hover:text-cyan-300 px-3 py-1.5 rounded-xl border border-slate-700 hover:border-cyan-500/40 transition-all active:scale-95">
                        🫀 Anatomía del corazón
                    </button>
                </div>
            </div>
        </div>

    </main>

    <!-- PANEL DE BÚSQUEDA FIJO (FOOTER SIEMPRE VISIBLE) -->
    <footer class="glass-card p-3 border-t border-slate-800/80 shrink-0 sticky bottom-0 z-50">
        <div class="max-w-2xl mx-auto flex items-center gap-2">
            <div class="relative flex-1">
                <input 
                    type="text" 
                    id="user-input" 
                    placeholder="Escribe tu consulta o tema de investigación..." 
                    onkeypress="manejarEnter(event)"
                    autocomplete="off"
                    class="glass-input w-full text-slate-100 placeholder-slate-500 text-sm rounded-2xl px-4 py-3.5 focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 transition-all shadow-inner"
                >
            </div>
            <button 
                onclick="enviarPregunta()" 
                class="bg-gradient-to-r from-cyan-500 to-teal-400 hover:from-cyan-400 hover:to-teal-300 active:scale-95 text-slate-950 font-bold p-3.5 rounded-2xl shadow-lg shadow-cyan-500/20 transition-all flex items-center justify-center shrink-0"
                title="Enviar mensaje"
            >
                <i data-lucide="send" class="w-5 h-5"></i>
            </button>
        </div>
    </footer>

    <!-- LÓGICA DE LA APLICACIÓN -->
    <script>
        // Inicialización de Iconos Lucide
        lucide.createIcons();

        // Base de conocimiento por defecto en caché offline
        let memoriaOffline = JSON.parse(localStorage.getItem('lucy_memoria')) || {
            "agua": "Sustancia H2O, fundamental para la vida y los procesos biológicos de los seres vivos.",
            "corazon": "Órgano muscular hueco que actúa como bomba impulsora del sistema circulatorio.",
            "celula": "Unidad fundamental, estructural y funcional de todos los organismos vivos."
        };

        // Guardar cambios en el almacenamiento local
        function guardarMemoriaLocal() {
            localStorage.setItem('lucy_memoria', JSON.stringify(memoriaOffline));
        }

        // Monitoreo en tiempo real del estado de red
        function actualizarEstadoRed() {
            const statusIndicator = document.getElementById('status-indicator');
            const statusText = document.getElementById('status-text');

            if (navigator.onLine) {
                statusIndicator.className = "absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 bg-emerald-400 rounded-full border-2 border-slate-950 pulse-cyan";
                statusText.className = "text-xs text-emerald-400 font-medium flex items-center gap-1";
                statusText.innerHTML = `<i data-lucide="wifi" class="w-3 h-3"></i> Red Global Activa`;
            } else {
                statusIndicator.className = "absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 bg-amber-400 rounded-full border-2 border-slate-950";
                statusText.className = "text-xs text-amber-400 font-medium flex items-center gap-1";
                statusText.innerHTML = `<i data-lucide="wifi-off" class="w-3 h-3"></i> Modo Offline`;
            }
            lucide.createIcons();
        }

        window.addEventListener('online', actualizarEstadoRed);
        window.addEventListener('offline', actualizarEstadoRed);
        actualizarEstadoRed();

        function usarSugerencia(texto) {
            document.getElementById('user-input').value = texto;
            enviarPregunta();
        }

        function limpiarChat() {
            const container = document.getElementById('chat-container');
            container.innerHTML = `
                <div class="text-center py-6">
                    <span class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-800/80 text-cyan-400 border border-slate-700/80">
                        ✨ Pantalla de chat limpiada
                    </span>
                </div>
            `;
        }

        function reiniciarMemoria() {
            memoriaOffline = {};
            localStorage.removeItem('lucy_memoria');
            agregarMensajeLucy("🗑️ Memoria caché local eliminada por completo.");
        }

        function manejarEnter(e) {
            if (e.key === 'Enter') enviarPregunta();
        }

        function agregarMensajeUsuario(texto) {
            const container = document.getElementById('chat-container');
            const html = `
                <div class="flex items-start justify-end gap-3">
                    <div class="bg-gradient-to-r from-cyan-600 to-teal-600 text-white p-3.5 rounded-2xl rounded-tr-sm max-w-[85%] text-sm leading-relaxed shadow-md">
                        ${escapeHtml(texto)}
                    </div>
                </div>
            `;
            container.insertAdjacentHTML('beforeend', html);
            scrollAlFondo();
        }

        function agregarMensajeLucy(texto) {
            const container = document.getElementById('chat-container');
            const id = 'lucy-msg-' + Date.now();
            const html = `
                <div class="flex items-start gap-3">
                    <div class="w-8 h-8 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 shrink-0 mt-1">
                        <i data-lucide="bot" class="w-4 h-4"></i>
                    </div>
                    <div id="${id}" class="glass-card p-4 rounded-2xl rounded-tl-sm max-w-[85%] text-sm leading-relaxed border border-slate-800 text-slate-200">
                        ${texto}
                    </div>
                </div>
            `;
            container.insertAdjacentHTML('beforeend', html);
            lucide.createIcons();
            scrollAlFondo();
            return id;
        }

        function mostrarCargando() {
            return agregarMensajeLucy(`
                <div class="flex items-center gap-2 text-cyan-400 font-medium">
                    <i data-lucide="loader-2" class="w-4 h-4 animate-spin"></i>
                    <span>Investigando en la red...</span>
                </div>
            `);
        }

        async function enviarPregunta() {
            const input = document.getElementById('user-input');
            const pregunta = input.value.trim();
            if (!pregunta) return;

            agregarMensajeUsuario(pregunta);
            input.value = '';

            const preguntaLower = pregunta.toLowerCase();

            // Comandos directos por consola de chat
            if (preguntaLower === 'limpiar') {
                limpiarChat();
                return;
            } else if (preguntaLower === 'borrar memoria') {
                reiniciarMemoria();
                return;
            }

            const tempId = mostrarCargando();

            if (navigator.onLine) {
                try {
                    // Filtro NLP Regex para quitar frases muletilla
                    let termino = preguntaLower
                        .replace(/que es el|que es la|que es|cual es el|cual es la|investiga sobre|investiga|busca sobre|busca|explicame|explica/g, '')
                        .trim();
                    if (!termino) termino = preguntaLower;

                    const urlBusqueda = `https://es.wikipedia.org/w/api.php?action=query&list=search&srsearch=${encodeURIComponent(termino)}&format=json&origin=*`;
                    const resBusq = await fetch(urlBusqueda);
                    const dataBusq = await resBusq.json();
                    const resultados = dataBusq.query?.search;

                    if (resultados && resultados.length > 0) {
                        const mejorTitulo = resultados[0].title;
                        const urlResumen = `https://es.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(mejorTitulo)}`;
                        const resRes = await fetch(urlResumen);
                        const dataRes = await resRes.json();

                        if (dataRes.extract) {
                            const tarjetaHTML = `
                                <div class="space-y-2">
                                    <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                                        <span class="font-bold text-cyan-400 text-sm font-heading">📌 ${mejorTitulo}</span>
                                        <span class="text-[9px] font-bold tracking-wider px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">RED GLOBAL</span>
                                    </div>
                                    <p class="text-slate-300 text-xs leading-relaxed">${dataRes.extract}</p>
                                </div>
                            `;
                            
                            document.getElementById(tempId).innerHTML = tarjetaHTML;
                            // Guardar en la caché persistente offline
                            memoriaOffline[preguntaLower] = `${mejorTitulo}: ${dataRes.extract}`;
                            guardarMemoriaLocal();
                            return;
                        }
                    }
                    throw new Error("Sin resultados de búsqueda");
                } catch (err) {
                    buscarEnMemoriaOffline(preguntaLower, tempId);
                }
            } else {
                buscarEnMemoriaOffline(preguntaLower, tempId);
            }
        }

        function buscarEnMemoriaOffline(preguntaLower, tempId) {
            let encontrado = false;
            for (let clave in memoriaOffline) {
                if (preguntaLower.includes(clave) || clave.includes(preguntaLower)) {
                    const tarjetaHTML = `
                        <div class="space-y-1.5">
                            <div class="flex items-center gap-1.5 text-amber-400 text-xs font-semibold">
                                <i data-lucide="wifi-off" class="w-3.5 h-3.5"></i>
                                <span>Respuesta obtenida de la Memoria Offline</span>
                            </div>
                            <p class="text-slate-300 text-xs leading-relaxed">${memoriaOffline[clave]}</p>
                        </div>
                    `;
                    document.getElementById(tempId).innerHTML = tarjetaHTML;
                    lucide.createIcons();
                    encontrado = true;
                    break;
                }
            }

            if (!encontrado) {
                document.getElementById(tempId).innerHTML = `
                    <p class="text-slate-400 text-xs flex items-center gap-2">
                        <span>⚠️ No se encontraron resultados en la red ni en la memoria caché local.</span>
                    </p>
                `;
            }
        }

        function scrollAlFondo() {
            const container = document.getElementById('chat-container');
            container.scrollTop = container.scrollHeight;
        }

        function escapeHtml(texto) {
            return texto.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        }
    </script>
</body>
</html>
```