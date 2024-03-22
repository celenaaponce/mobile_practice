import streamlit as st
import inspect
from importlib import import_module
from pathlib import Path
from typing import Any, Callable, Optional, TypeVar, Union, overload

try:
    from streamlit.runtime.metrics_util import gather_metrics as _gather_metrics
except ImportError:

    def _gather_metrics(name, func):  # type: ignore
        return func


F = TypeVar("F", bound=Callable[..., Any])

# Typing overloads here are actually required so that you can correctly (= with correct typing) use the decorator in different ways:
#   1) as a decorator without parameters @extra
#   2) as a decorator with parameters (@extra(foo="bar") but this also refers to empty parameters @extra()
#   3) as a function: extra(my_function)


@overload
def extra(
    func: F,
) -> F:
    ...


@overload
def extra(
    func: None = None,
) -> Callable[[F], F]:
    ...


def extra(
    func: Optional[F] = None,
) -> Union[Callable[[F], F], F]:

    if func:

        filename = inspect.stack()[1].filename
        submodule = Path(filename).parent.name
        extra_name = "streamlit_extras." + submodule
        module = import_module(extra_name)

        if hasattr(module, "__funcs__"):
            module.__funcs__ += [func]  # type: ignore
        else:
            module.__funcs__ = [func]  # type: ignore

        profiling_name = f"{submodule}.{func.__name__}"
        try:
            return _gather_metrics(name=profiling_name, func=func)
        except TypeError:
            # Don't fail on streamlit==1.13.0, which only expects a callable
            pass

    def wrapper(f: F) -> F:
        return f

    return wrapper


@extra
def switch_page(page_name: str, extra = None):
    """
    Switch page programmatically in a multipage app

    Args:
        page_name (str): Target page name
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")





__title__ = "Switch page function"
__desc__ = "Function to switch page programmatically in a MPA"
__icon__ = "🖱️"
__author__ = "Zachary Blackwood"
__stlite__ = False
