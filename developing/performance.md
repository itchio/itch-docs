# Diving into performance

## Chrome DevTools

Chrome has many tools that let us know what we're doing.

First off, don't check **Hide Violations**. Violations are bad, let's not do them.

They may happen when first-time-loading large datasets, that's okay - but in normal, we-have-almost-everything-cached state, they shouldn't happen.

Use the **Performance** tab to see where time is spent, including React rendering:

![](/assets/profile-react.png)

Get to know the tools. They're good.

## React performance tips

In short:

* Use `React.memo` to wrap your functional components. It serves the same purpose as `React.PureComponent` but for functional components, preventing unnecessary re-renders by using a shallow comparison of props.

* For connected components, use hooks like `useSelector` from `react-redux` to listen only the least set of dependent values to avoid re-renders

```javascript
import React, { memo } from 'react';
import { useAppDispatch, useAppSelector } from "renderer/hooks/redux";

const SomeComponent = () => {
  const dispatch = useAppDispatch();
  const appVersion = useAppSelector((rs) => rs.system.appVersion);

  const handleButtonClick = useCallback(() => {
    dispatch({ type: 'DO_SOMETHING' });
  }, [dispatch]);

  return <button onClick={handleButtonClick}>{appVersion}</button>;
};

export default memo(SomeComponent);
```

* Avoid using anonymous functions in render when passing into sub-components so that they make take advantage of memoization. Instead, use stable references with `useCallback` which will return a memoized version of the callback that only changes if one of the dependencies has changed.

```javascript
import React, { memo, useCallback } from 'react';

// Bad approach
const BadComponent = memo(() => {
  const doStuff = () => {
    // stuff.
  };

  // This will force MyComplexComponent to always re-render
  return <MyComplexComponent onClick={doStuff}/>;
});

// Good practice
const GoodComponent = memo(() => {
  const doStuff = useCallback(() => {
    // stuff.
  }, []); // Dependencies array

  // Memoized `doStuff` won't trigger unnecessary renders when GoodComponent is re-rerendered
  return <div onClick={doStuff}/>;
});
```

By using hooks and keeping function references stable with `useCallback`, you
allow React's memoization strategies to optimize your component rendering. This
helps in performance gains by reducing unnecessary rendering.

