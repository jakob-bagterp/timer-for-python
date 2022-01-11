class TimerForPython < Formula
  include Language::Python::Virtualenv

  desc "Makes it easy to measure time and performance of Python programs"
  homepage "https://github.com/jakob-bagterp/timer-for-python"
  url "https://github.com/jakob-bagterp/timer-for-python/releases/download/v0.3.4/timer-for-python-0.3.4.tar.gz"
  sha256 "ab64da1a76157f56595fc972016fc260d5467e5f66e3dce5b4fb20fd002da322"
  license "MIT"

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "true"
  end
end
