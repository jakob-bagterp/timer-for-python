class TimerForPython < Formula
  desc "Makes it easy to measure how much time it takes to run Python programs"
  homepage "https://github.com/jakob-bagterp/timer_for_python"
  url "https://github.com/jakob-bagterp/timer_for_python/releases/download/v0.3.3/timer_for_python-0.3.3.tar.gz"
  sha256 "71f49d1b98fb05dbc572a34c2edf1411fbf42ab4ba0063e2bf7c9cb36cf38d98"
  license "MIT"

  depends_on "python@3.8"

  def install
    bin.install "timer-for-python"
  end

  test do
    system "false"
  end
end
