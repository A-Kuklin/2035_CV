from fastapi import APIRouter

from .action import router as action_router
from .data_links import router as data_links_router
from .specialization import router as specialization_router
from .tool import router as tool_router


router = APIRouter()
router.include_router(action_router)
router.include_router(specialization_router)
router.include_router(tool_router)
router.include_router(data_links_router)
