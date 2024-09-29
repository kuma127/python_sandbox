use pyo3::prelude::*;

#[pyfunction]
fn count_chars(s: &str) -> (usize, usize, usize) {
    // カウント用変数定義
    let mut alphabet_count = 0;
    let mut digit_count = 0;
    let mut other_count = 0;

    for c in s.chars() {
        if c.is_ascii_alphabetic() {
            alphabet_count += 1;
        } else if c.is_ascii_digit() {
            digit_count += 1;
        } else {
            other_count += 1;
        }
    }

    (alphabet_count, digit_count, other_count)
}

/// A Python module implemented in Rust.
#[pymodule]
fn strcounter(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(count_chars, m)?)?;
    Ok(())
}
