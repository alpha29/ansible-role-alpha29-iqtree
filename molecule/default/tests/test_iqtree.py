def test_iqtree(host):
    """
    Check iqtree version.
    """
    cmd = "iqtree --version"
    cmd_result = host.run(cmd)
    assert cmd_result.rc == 0, "'{}' returned status {}.".format(cmd, cmd_result.rc)
    assert "1.6.12" in cmd_result.stdout, f"'{cmd}' returned stdout '{cmd_result.stdout}', stderr '{cmd_result.stderr}'"
