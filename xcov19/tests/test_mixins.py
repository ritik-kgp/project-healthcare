import unittest
from xcov19.utils.mixins import InterfaceProtocolCheckMixin

class TestInterfaceProtocolCheckMixin(unittest.TestCase):

    def test_implementation_with_all_methods(self):
        class Interface:
            def method1(self): pass

        class Implementation(InterfaceProtocolCheckMixin, Interface):
            def method1(self): pass

        try:
            Implementation()
        except NotImplementedError:
            self.fail("NotImplementedError raised when it shouldn't have been.")
    
    def test_missing_method_in_implementation(self):
        class Interface:
            def method1(self): pass

        class Implementation(InterfaceProtocolCheckMixin, Interface):
            pass

        with self.assertRaises(NotImplementedError):
            Implementation()
    
    def test_extra_method_in_implementation(self):
        class Interface:
            def method1(self): pass

        class Implementation(InterfaceProtocolCheckMixin, Interface):
            def method1(self): pass
            def extra_method(self): pass

        try:
            Implementation()  # Extra method should not raise an error.
        except NotImplementedError:
            self.fail("NotImplementedError raised due to an extra method, which should be allowed.")
    
    def test_signature_mismatch(self):
        class Interface:
            def method1(self, a): pass

        class Implementation(InterfaceProtocolCheckMixin, Interface):
            def method1(self, b): pass

        with self.assertRaises(NotImplementedError):
            Implementation()

if __name__ == '__main__':
    unittest.main()
