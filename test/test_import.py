def test_import_package():
    """Test that the package has the expected structure."""
    import isaac_sim_demo

    # Check that __version__ exists
    assert hasattr(
        isaac_sim_demo, "__version__"
    ), "Package should have __version__ attribute"


def test_import_core():
    """Test that the core module can be imported."""
    from isaac_sim_demo import core

    assert core is not None
