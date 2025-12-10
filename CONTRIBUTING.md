# Contributing to Real-Time Currency Converter

Thank you for your interest in contributing to this project! We appreciate all contributions, whether they're bug reports, feature suggestions, documentation improvements, or code changes.

## Code of Conduct

Please be respectful and constructive in all interactions with other contributors.

## How to Contribute

### 1. Report Bugs

Found a bug? Please open an issue with:
- Clear title describing the bug
- Detailed description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)

### 2. Suggest Features

Have a feature idea? Open an issue with:
- Clear title for the feature
- Detailed description
- Why you think it would be useful
- Possible implementation approach

### 3. Submit Code Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Real-Time-Currency-Converter.git
   cd Real-Time-Currency-Converter
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Update documentation as needed

4. **Test your changes**
   ```bash
   python app.py
   # Test the feature manually
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add descriptive commit message"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Write a clear PR description
   - Submit the PR

## Code Style Guidelines

### Python Code
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable names
- Keep functions focused and small
- Add docstrings to functions

Example:
```python
def get_conversion_rate(from_currency, to_currency):
    """
    Fetch the conversion rate between two currencies.
    
    Args:
        from_currency (str): Source currency code
        to_currency (str): Target currency code
    
    Returns:
        float: Exchange rate or None if failed
    """
    # Implementation here
    pass
```

### JavaScript Code
- Use const/let (avoid var)
- Add comments for complex logic
- Use meaningful names for variables and functions

### HTML/CSS
- Use semantic HTML elements
- Keep CSS organized
- Use classes for styling (avoid inline styles)

## Testing

Before submitting a PR:
1. Test the application manually
2. Check for console errors
3. Test on different browsers
4. Verify responsive design

## Documentation

- Update README.md if adding features
- Document API changes
- Add comments to complex code
- Update this CONTRIBUTING.md if needed

## Commit Message Guidelines

Write clear, descriptive commit messages:

- Use imperative mood ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Add more details in the body if needed
- Reference issues when applicable

Examples:
```
Add dark mode toggle
Fix currency conversion error when amount is zero
Update API endpoint to v2
```

## Pull Request Process

1. **Update documentation** - Update README.md and other docs
2. **Test thoroughly** - Verify all functionality works
3. **Keep changes focused** - One feature per PR
4. **Write clear description** - Explain what and why
5. **Be responsive** - Respond to review comments promptly

## Areas for Contribution

- [ ] Feature implementations
- [ ] Bug fixes
- [ ] Documentation improvements
- [ ] Performance optimizations
- [ ] UI/UX enhancements
- [ ] Testing and test coverage
- [ ] Accessibility improvements
- [ ] Internationalization (i18n)

## Questions?

Feel free to open a discussion or issue if you have questions about contributing.

Thank you for making this project better! 🙏
