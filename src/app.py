from r2r.main import E2EPipelineFactory, R2RConfig

from .ionic_rag import IonicProductPipeline

app = E2EPipelineFactory.create_pipeline(
    rag_pipeline_impl=IonicProductPipeline,
    config=R2RConfig.load_config("config.json"), 
)

# uvicorn src.app:app --reload