import inspect

class InterfaceProtocolCheckMixin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        for base in cls.__bases__:
            if issubclass(base, InterfaceProtocolCheckMixin):
                continue

            for name, method in inspect.getmembers(base, predicate=inspect.isfunction):
                if not callable(getattr(cls, name, None)):
                    raise NotImplementedError(f"Method '{name}' is declared in interface '{base.__name__}' but not implemented in '{cls.__name__}'")
                    
                # Check method signature
                interface_method = getattr(base, name)
                impl_method = getattr(cls, name)
                
                interface_signature = inspect.signature(interface_method)
                impl_signature = inspect.signature(impl_method)
                
                if interface_signature != impl_signature:
                    raise NotImplementedError(f"Signature for '{name}' not correct:\n"
                                              f"Expected: {interface_signature}\n"
                                              f"Got: {impl_signature}\n")
