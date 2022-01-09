class TimerForPython < Formula
  include Language::Python::Virtualenv

  desc "Makes it easy to measure time and performance of Python programs"
  homepage "https://github.com/jakob-bagterp/timer-for-python"
  url "https://github.com/jakob-bagterp/timer-for-python/releases/download/v0.3.3/timer_for_python-0.3.3.tar.gz"
  sha256 "71f49d1b98fb05dbc572a34c2edf1411fbf42ab4ba0063e2bf7c9cb36cf38d98"
  license "MIT"

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "true"
  end
end
