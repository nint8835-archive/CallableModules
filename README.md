# CallableModules - Callable modules for python
Ever wished that you could make your module callable? Now you can! All you need to do is:

```python
import CallableModules


def __call__(*args, **kwargs):
    # Your code goes here

CallableModules.patch()
```

That's it. That's all you need to do. Bam. Your module now also works as a function.

Alternatively, if you want to use a callable module to make your module callable:
```python
import CallableModules


def __call__(*args, **kwargs):
    # Your code goes here

CallableModules()
```

# Disclaimer
This module breaks like every rule and is held together with used chewing gum and dreams. I wouldn't suggest using this for anything mission-critical. You're welcome to if that makes you happy, but don't come to me if it causes issues. That's your problem, not mine.