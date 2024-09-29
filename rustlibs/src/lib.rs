use pyo3::prelude::*;

mod hello;

use hello::sum_as_string;
use hello::hello_world;

/// A Python module implemented in Rust.
#[pymodule]
fn rustlibs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(hello_world, m)?)?;
    Ok(())
}
