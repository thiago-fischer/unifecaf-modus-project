import { useMemo, useState } from "react";
import { MetricCard } from "./components/MetricCard";
import { modelOptions } from "./data/models";
import "./App.css";

const tasks = ["Resumo de texto", "Criação de conteúdo", "Busca orientada"];
const outputSizes = ["Curta", "Média", "Longa"];

function App() {
  const [selectedModel, setSelectedModel] = useState(modelOptions[0].name);
  const [task, setTask] = useState(tasks[0]);
  const [outputSize, setOutputSize] = useState(outputSizes[1]);

  const selected = useMemo(
    () =>
      modelOptions.find((item) => item.name === selectedModel) ??
      modelOptions[0],
    [selectedModel],
  );

  const multiplierMap: Record<string, number> = {
    Curta: 0.7,
    Média: 1,
    Longa: 1.6,
  };

  const multiplier = multiplierMap[outputSize] ?? 1;

  const estimatedInput = Math.round(selected.inputTokens * multiplier);
  const estimatedOutput = Math.round(selected.outputTokens * multiplier);
  const estimatedCost = Number(
    (selected.estimatedCost * multiplier).toFixed(2),
  );

  return (
    <main className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">Modus</p>
          <h1>Estimador de custo de IA</h1>
        </div>
        <button type="button" className="ghost-button">
          Comparar modelos
        </button>
      </header>

      <section className="panel hero-panel">
        <div className="hero-copy">
          <span className="status-pill">Versão MVP</span>
          <h2>Entenda o custo por trás de uma interação com LLM.</h2>
          <p>
            Simule uma tarefa, escolha um modelo e veja o impacto estimado em
            tokens, custo e uso consciente de IA.
          </p>
        </div>

        <div className="simulation-form">
          <label>
            Modelo
            <select
              value={selectedModel}
              onChange={(event) => setSelectedModel(event.target.value)}
            >
              {modelOptions.map((model) => (
                <option key={model.name} value={model.name}>
                  {model.name}
                </option>
              ))}
            </select>
          </label>

          <label>
            Tipo de tarefa
            <select
              value={task}
              onChange={(event) => setTask(event.target.value)}
            >
              {tasks.map((item) => (
                <option key={item} value={item}>
                  {item}
                </option>
              ))}
            </select>
          </label>

          <label>
            Tamanho da resposta
            <select
              value={outputSize}
              onChange={(event) => setOutputSize(event.target.value)}
            >
              {outputSizes.map((item) => (
                <option key={item} value={item}>
                  {item}
                </option>
              ))}
            </select>
          </label>
        </div>
      </section>

      <section className="metrics-grid">
        <MetricCard
          label="Tokens de entrada"
          value={`${estimatedInput.toLocaleString()} tk`}
          detail="Contexto do prompt"
        />
        <MetricCard
          label="Tokens de saída"
          value={`${estimatedOutput.toLocaleString()} tk`}
          detail="Resposta gerada"
        />
        <MetricCard
          label="Custo estimado"
          value={`US$ ${estimatedCost.toFixed(2)}`}
          detail="Aproximado por solicitação"
        />
      </section>

      <section className="content-grid">
        <article className="panel model-panel">
          <div className="panel-header">
            <h3>Modelo selecionado</h3>
            <span>{selected.name}</span>
          </div>

          <ul className="model-info">
            <li>
              <strong>Tarefa</strong>
              <span>{selected.task}</span>
            </li>
            <li>
              <strong>Uso recomendado</strong>
              <span>{selected.context}</span>
            </li>
            <li>
              <strong>Contexto</strong>
              <span>{selected.context}</span>
            </li>
          </ul>
        </article>

        <article className="panel insights-panel">
          <div className="panel-header">
            <h3>Orientação prática</h3>
          </div>

          <ul className="tips-list">
            <li>Reduza prompts redundantes para diminuir tokens de entrada.</li>
            <li>
              Defina uma resposta mais curta quando a qualidade for suficiente.
            </li>
            <li>Compare modelos antes de escalar automações internas.</li>
          </ul>
        </article>
      </section>
    </main>
  );
}

export default App;
