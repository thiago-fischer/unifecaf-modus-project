import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { MetricCard } from "./components/MetricCard";
import {
  createSimulation,
  getCatalog,
  type Catalog,
  type Simulation,
  type SimulationChoices,
} from "./services/modusApi";
import heroImage from "./assets/hero.png";
import "./App.css";

const formatTokens = (value: number) => new Intl.NumberFormat("pt-BR").format(value);
const formatCost = (value: number) => `US$ ${value.toFixed(6)}`;

function App() {
  const [catalog, setCatalog] = useState<Catalog | null>(null);
  const [catalogError, setCatalogError] = useState("");
  const [reloadCatalog, setReloadCatalog] = useState(0);
  const [choices, setChoices] = useState<SimulationChoices>({
    modelId: "",
    taskType: "",
    responseSize: "",
  });
  const [simulation, setSimulation] = useState<Simulation | null>(null);
  const [simulationError, setSimulationError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showComparison, setShowComparison] = useState(false);

  useEffect(() => {
    const controller = new AbortController();
    getCatalog(controller.signal)
      .then((data) => {
        if (!data.models.length || !data.taskTypes.length || !data.responseSizes.length) {
          throw new Error("O catálogo está vazio. Tente novamente mais tarde.");
        }
        setCatalog(data);
        setCatalogError("");
        setChoices({
          modelId: data.models.find((model) => model.id === "modus-equilibrado")?.id ?? data.models[0].id,
          taskType: data.taskTypes[0].id,
          responseSize: data.responseSizes.find((size) => size.id === "medium")?.id ?? data.responseSizes[0].id,
        });
      })
      .catch((error: unknown) => {
        if (controller.signal.aborted) return;
        setCatalogError(
          error instanceof Error ? error.message : "Não foi possível carregar o catálogo.",
        );
      });
    return () => controller.abort();
  }, [reloadCatalog]);

  function updateChoice(field: keyof SimulationChoices, value: string) {
    setChoices((current) => ({ ...current, [field]: value }));
    setSimulation(null);
    setSimulationError("");
    setShowComparison(false);
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!catalog || isSubmitting) return;
    setIsSubmitting(true);
    setSimulationError("");
    setSimulation(null);
    setShowComparison(false);
    try {
      setSimulation(await createSimulation(choices));
    } catch (error) {
      setSimulationError(
        error instanceof Error ? error.message : "Não foi possível simular. Tente novamente.",
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  const selectedModel = catalog?.models.find((model) => model.id === choices.modelId);
  const selectedTask = catalog?.taskTypes.find((task) => task.id === choices.taskType);
  const selectedSize = catalog?.responseSizes.find((size) => size.id === choices.responseSize);

  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="#inicio" aria-label="Modus, voltar ao início">
          <span className="brand-mark" aria-hidden="true">M</span>
          <span>modus<span className="brand-dot">.</span></span>
        </a>
        <span className="topbar-note">Uma forma mais consciente de usar IA</span>
      </header>

      <main id="inicio">
        <section className="hero" aria-labelledby="hero-title">
          <div className="hero-copy">
            <span className="eyebrow"><span className="eyebrow-line" /> SIMULADOR EDUCATIVO</span>
            <h1 id="hero-title">Toda resposta tem um <em>custo.</em></h1>
            <p>
              Entenda como o modelo, a tarefa e o tamanho da resposta influenciam
              os tokens e o custo estimado de uma interação com IA.
            </p>
            <a className="text-link" href="#simulador">Começar simulação <span aria-hidden="true">↗</span></a>
          </div>
          <div className="hero-art" aria-hidden="true">
            <div className="hero-orbit hero-orbit-one" />
            <div className="hero-orbit hero-orbit-two" />
            <img src={heroImage} alt="" />
            <span className="hero-art-label">ENTRADA <b>→</b> RESPOSTA</span>
          </div>
        </section>

        <section className="workspace" id="simulador" aria-labelledby="simulator-title">
          <div className="section-heading">
            <div>
              <span className="step-label">01 / EXPLORE</span>
              <h2 id="simulator-title">Monte seu cenário</h2>
              <p>Escolha as opções e gere uma estimativa. Nenhum prompt é enviado.</p>
            </div>
            <span className="section-badge">Sem cadastro · Sem chave de API</span>
          </div>

          <div className="simulator-card">
            <form onSubmit={handleSubmit}>
              <div className="form-grid">
                <label htmlFor="model">Modelo <span>01</span></label>
                <select
                  id="model"
                  value={choices.modelId}
                  onChange={(event) => updateChoice("modelId", event.target.value)}
                  disabled={!catalog || isSubmitting}
                  required
                >
                  {!catalog && <option value="">Carregando modelos...</option>}
                  {catalog?.models.map((model) => <option key={model.id} value={model.id}>{model.name}</option>)}
                </select>

                <label htmlFor="task">Tipo de tarefa <span>02</span></label>
                <select
                  id="task"
                  value={choices.taskType}
                  onChange={(event) => updateChoice("taskType", event.target.value)}
                  disabled={!catalog || isSubmitting}
                  required
                >
                  {!catalog && <option value="">Carregando tarefas...</option>}
                  {catalog?.taskTypes.map((task) => <option key={task.id} value={task.id}>{task.name}</option>)}
                </select>

                <label htmlFor="size">Tamanho da resposta <span>03</span></label>
                <select
                  id="size"
                  value={choices.responseSize}
                  onChange={(event) => updateChoice("responseSize", event.target.value)}
                  disabled={!catalog || isSubmitting}
                  required
                >
                  {!catalog && <option value="">Carregando tamanhos...</option>}
                  {catalog?.responseSizes.map((size) => <option key={size.id} value={size.id}>{size.name}</option>)}
                </select>
              </div>

              <div className="form-footer">
                <p>Valores fixos para fins educativos, em dólar americano.</p>
                <button className="primary-button" type="submit" disabled={!catalog || isSubmitting}>
                  {isSubmitting ? "Calculando..." : "Simular custo"}<span aria-hidden="true">→</span>
                </button>
              </div>
            </form>
            {catalogError && (
              <div className="message error-message" role="alert">
                <span>{catalogError}</span>
                <button type="button" onClick={() => setReloadCatalog((value) => value + 1)}>Tentar novamente</button>
              </div>
            )}
            {simulationError && <p className="message error-message" role="alert">{simulationError}</p>}
          </div>
        </section>

        <section className="results" aria-labelledby="results-title" aria-live="polite">
          <div className="section-heading result-heading">
            <div>
              <span className="step-label">02 / ENTENDA</span>
              <h2 id="results-title">Resultado da simulação</h2>
            </div>
            {simulation && <span className="section-badge">{selectedTask?.name} · resposta {selectedSize?.name.toLowerCase()}</span>}
          </div>

          {simulation ? (
            <>
              <div className="result-intro">
                <div>
                  <span className="result-kicker">CENÁRIO SELECIONADO</span>
                  <h3>{selectedModel?.name ?? simulation.estimate.modelName}</h3>
                </div>
                <span className="estimate-tag">Estimativa · {simulation.currency}</span>
              </div>
              <div className="metrics-grid">
                <MetricCard label="Tokens de entrada" value={formatTokens(simulation.estimate.inputTokens)} detail="Contexto estimado da tarefa" />
                <MetricCard label="Tokens de saída" value={formatTokens(simulation.estimate.outputTokens)} detail="Tamanho estimado da resposta" />
                <MetricCard label="Total de tokens" value={formatTokens(simulation.estimate.totalTokens)} detail="Entrada + saída" />
                <MetricCard label="Custo estimado" value={formatCost(simulation.estimate.cost)} detail="Por uma interação" />
              </div>

              <div className="comparison-actions">
                <div>
                  <h3>Compare as possibilidades</h3>
                  <p>A mesma tarefa e resposta, em cada modelo do catálogo.</p>
                </div>
                <button
                  className="outline-button"
                  type="button"
                  aria-expanded={showComparison}
                  aria-controls="comparison"
                  onClick={() => setShowComparison((current) => !current)}
                >
                  {showComparison ? "Ocultar comparação" : "Comparar modelos"}<span aria-hidden="true">{showComparison ? "−" : "+"}</span>
                </button>
              </div>

              {showComparison && (
                <div className="comparison-wrap" id="comparison">
                  <table className="comparison-table">
                    <caption>Comparação para {selectedTask?.name.toLowerCase()} com resposta {selectedSize?.name.toLowerCase()}</caption>
                    <thead><tr><th scope="col">Modelo</th><th scope="col">Entrada</th><th scope="col">Saída</th><th scope="col">Total</th><th scope="col">Custo estimado</th></tr></thead>
                    <tbody>
                      {simulation.comparison.map((item) => (
                        <tr key={item.modelId} className={item.selected ? "selected-row" : ""}>
                          <th scope="row">{item.modelName}{item.selected && <span className="row-tag">Selecionado</span>}</th>
                          <td>{formatTokens(item.inputTokens)}</td>
                          <td>{formatTokens(item.outputTokens)}</td>
                          <td>{formatTokens(item.totalTokens)}</td>
                          <td>{formatCost(item.cost)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                  <p className="comparison-note">O menor custo não indica, por si só, o melhor modelo para a tarefa.</p>
                </div>
              )}

              <div className="guidance-card">
                <div><span className="step-label">03 / REFLITA</span><h3>Use com intenção</h3></div>
                <ul>{simulation.guidance.map((tip) => <li key={tip}>{tip}</li>)}</ul>
              </div>
              <p className="disclaimer"><strong>Sobre esta estimativa.</strong> {simulation.disclaimer} {catalog?.disclaimer}</p>
            </>
          ) : (
            <div className="empty-state">
              <span aria-hidden="true">↗</span>
              <p>{isSubmitting ? "Calculando sua estimativa..." : "Sua estimativa aparecerá aqui após a simulação."}</p>
            </div>
          )}
        </section>
      </main>

      <footer className="footer"><span>modus<span className="brand-dot">.</span></span><p>Transparência para escolhas melhores.</p><span>MVP EDUCATIVO</span></footer>
    </div>
  );
}

export default App;
