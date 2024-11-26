local posix = require("posix")
local os_time = os.time
local function sleep(seconds) posix.nanosleep(seconds) end -- Simula o time.sleep

-- Função executada pelos filhos
local function tarefa_filho(numero)
    local pid = posix.getpid("pid")
    local ppid = posix.getpid("ppid")
    local inicio = os.date("%H:%M:%S", os_time())

    print(string.rep("=", 40))
    print(string.format("[FILHO] Iniciando processo filho\nPID: %d | Pai: %d | Início: %s", pid, ppid, inicio))
    print(string.format("[FILHO] PID: %d | Tarefa: Calculando %d²", pid, numero))
    print(string.rep("=", 40))

    sleep(2) -- Simula execução
    local resultado = numero ^ 2

    local fim = os.date("%H:%M:%S", os_time())
    print(string.format("[FILHO] PID: %d | Resultado: %d² = %d", pid, numero, resultado))
    print(string.format("[FILHO] PID: %d | Finalizando processo | Fim: %s", pid, fim))
    print(string.rep("=", 40))
end

-- Função para criar e gerenciar os processos
local function criar_processos(num_processos)
    local pai_pid = posix.getpid("pid")
    print(string.rep("#", 50))
    print(string.format("[PAI] PID: %d | Criando %d processos filhos", pai_pid, num_processos))
    print(string.rep("#", 50))

    local filhos = {}

    for i = 1, num_processos do
        local pid = posix.fork()
        if pid == 0 then
            -- Processo filho executa sua tarefa
            tarefa_filho(i)
            os.exit() -- Termina o processo filho
        elseif pid > 0 then
            -- Processo pai adiciona o filho à tabela de controle
            table.insert(filhos, pid)
            print(string.format("[PAI] Processo filho %d iniciado | PID: %d", i, pid))
            sleep(0.1) -- Pausa para ajuste na saída
        else
            print("[PAI] Erro ao criar processo filho")
            os.exit(1)
        end
    end

    print("\n[PAI] Todos os processos filhos foram criados. Aguardando finalização...")
    print(string.rep("-", 50))

    -- O pai espera todos os filhos terminarem
    for _, pid in ipairs(filhos) do
        local _, status = posix.wait(pid)
        if status == 0 then
            print(string.format("[PAI] Processo filho concluído | PID: %d", pid))
        else
            print(string.format("[PAI] Erro no processo filho | PID: %d", pid))
        end
    end

    print(string.rep("#", 50))
    print("[PAI] Todos os processos foram finalizados.")
    print(string.rep("#", 50))
end

-- Função principal
local function main()
    print("\n==== INÍCIO DO GERENCIAMENTO DE PROCESSOS ====\n")
    local num_processos = 3
    criar_processos(num_processos)
    print("\n==== PROGRAMA ENCERRADO ====\n")
end

main()
