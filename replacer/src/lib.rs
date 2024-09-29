use pyo3::prelude::*;
use regex::Regex;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn replace_with_pattern(pattern: &str, text: &str, replacement: &str) -> String {
    let re = Regex::new(pattern).unwrap();
    re.replace_all(text, replacement).to_string()
}

/// A Python module implemented in Rust.
#[pymodule]
fn replacer(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(replace_with_pattern, m)?)?;
    Ok(())
}
