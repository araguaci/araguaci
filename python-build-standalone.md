  Python Standalone Builds — python-build-standalone documentation       

Python Standalone Builds[¶](#python-standalone-builds "Permalink to this heading")
==================================================================================

This project produces self-contained, highly-portable Python distributions. These Python distributions contain a fully-usable, full-featured Python installation: most extension modules from the Python standard library are present and their library dependencies are either distributed with the distribution or are statically linked.

The Python distributions are built in a manner to minimize run-time dependencies. This includes limiting the CPU instructions that can be used and limiting the set of shared libraries required at run-time. The goal is for the produced distribution to work on any system for the targeted architecture.

Some distributions ship with their build artifacts (object files, libraries, etc) along with rich metadata describing the distribution and how it was assembled. The build artifacts can be recombined by downstream repackagers to derive a custom Python distribution, possibly without certain features like SQLite and OpenSSL. This is useful for embedding Python in a larger binary. See the [PyOxidizer](https://github.com/indygreg/PyOxidizer) sister project for such a downstream repackager.

Many users of these distributions might be better served by the [PyOxy](https://pyoxidizer.readthedocs.io/en/latest/pyoxy.html) sister project. PyOxy takes these Python distributions and adds some Rust code for enhancing the functionality of the Python interpreter. The official PyOxy release binaries are single file executables providing a full-featured Python interpreter.

Contents:

*   [Running Distributions](https://gregoryszorc.com/docs/python-build-standalone/main/running.html)
    *   [Obtaining Distributions](https://gregoryszorc.com/docs/python-build-standalone/main/running.html#obtaining-distributions)
    *   [Extracting Distributions](https://gregoryszorc.com/docs/python-build-standalone/main/running.html#extracting-distributions)
    *   [Runtime Requirements](https://gregoryszorc.com/docs/python-build-standalone/main/running.html#runtime-requirements)
    *   [Extra Python Software](https://gregoryszorc.com/docs/python-build-standalone/main/running.html#extra-python-software)
    *   [Licensing](https://gregoryszorc.com/docs/python-build-standalone/main/running.html#licensing)
    *   [Reconsuming Build Artifacts](https://gregoryszorc.com/docs/python-build-standalone/main/running.html#reconsuming-build-artifacts)
*   [Building](https://gregoryszorc.com/docs/python-build-standalone/main/building.html)
    *   [Linux](https://gregoryszorc.com/docs/python-build-standalone/main/building.html#linux)
    *   [macOS](https://gregoryszorc.com/docs/python-build-standalone/main/building.html#macos)
    *   [Windows](https://gregoryszorc.com/docs/python-build-standalone/main/building.html#windows)
    *   [Using sccache to Speed up Builds](https://gregoryszorc.com/docs/python-build-standalone/main/building.html#using-sccache-to-speed-up-builds)
*   [Behavior Quirks](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html)
    *   [Backspace Key Doesn’t work in Python REPL](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#backspace-key-doesn-t-work-in-python-repl)
    *   [No tix on macOS](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#no-tix-on-macos)
    *   [No `pip.exe` on Windows](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#no-pip-exe-on-windows)
    *   [Windows Static Distributions are Extremely Brittle](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#windows-static-distributions-are-extremely-brittle)
    *   [Linking Static Library on macOS](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#linking-static-library-on-macos)
    *   [Use of `libedit` on Linux](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#use-of-libedit-on-linux)
    *   [Static Linking of musl libc Prevents Extension Module Library Loading](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#static-linking-of-musl-libc-prevents-extension-module-library-loading)
    *   [Static Linking of `libX11` / Incompatibility with PyQt on Linux](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#static-linking-of-libx11-incompatibility-with-pyqt-on-linux)
    *   [Missing `libcrypt.so.1`](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#missing-libcrypt-so-1)
    *   [References to Build-Time Paths](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html#references-to-build-time-paths)
*   [Technical Notes](https://gregoryszorc.com/docs/python-build-standalone/main/technotes.html)
    *   [How It Works](https://gregoryszorc.com/docs/python-build-standalone/main/technotes.html#how-it-works)
    *   [Setup.local Hackery](https://gregoryszorc.com/docs/python-build-standalone/main/technotes.html#setup-local-hackery)
    *   [Dependency Notes](https://gregoryszorc.com/docs/python-build-standalone/main/technotes.html#dependency-notes)
    *   [Upgrading CPython](https://gregoryszorc.com/docs/python-build-standalone/main/technotes.html#upgrading-cpython)
*   [Distribution Archives](https://gregoryszorc.com/docs/python-build-standalone/main/distributions.html)
    *   [Full Archive](https://gregoryszorc.com/docs/python-build-standalone/main/distributions.html#full-archive)
    *   [Install Only Archive](https://gregoryszorc.com/docs/python-build-standalone/main/distributions.html#install-only-archive)
*   [Project Status](https://gregoryszorc.com/docs/python-build-standalone/main/status.html)
    *   [Target Notes](https://gregoryszorc.com/docs/python-build-standalone/main/status.html#target-notes)
    *   [Test Failures](https://gregoryszorc.com/docs/python-build-standalone/main/status.html#test-failures)
    *   [Test Skips](https://gregoryszorc.com/docs/python-build-standalone/main/status.html#test-skips)

Indices and tables[¶](https://gregoryszorc.com/docs/python-build-standalone/main/#indices-and-tables "Permalink to this heading")
======================================================================

*   [Index](https://gregoryszorc.com/docs/python-build-standalone/main/genindex.html)
    
*   [Search Page](https://gregoryszorc.com/docs/python-build-standalone/main/search.html)
    

[python-build-standalone](https://gregoryszorc.com/docs/python-build-standalone/main/#)
============================

### Navigation

Contents:

*   [Running Distributions](https://gregoryszorc.com/docs/python-build-standalone/main/running.html)
*   [Building](https://gregoryszorc.com/docs/python-build-standalone/main/building.html)
*   [Behavior Quirks](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html)
*   [Technical Notes](https://gregoryszorc.com/docs/python-build-standalone/main/technotes.html)
*   [Distribution Archives](https://gregoryszorc.com/docs/python-build-standalone/main/distributions.html)
*   [Project Status](https://gregoryszorc.com/docs/python-build-standalone/main/status.html)

### Related Topics

*   [Documentation overview](https://gregoryszorc.com/docs/python-build-standalone/main/#)
    *   Next: [Running Distributions](https://gregoryszorc.com/docs/python-build-standalone/main/running.html "next chapter")

### Quick search

 

document.getElementById('searchbox').style.display = "block"

©2020, Gregory Szorc. | Powered by [Sphinx 5.0.2](http://sphinx-doc.org/) & [Alabaster 0.7.12](https://github.com/bitprophet/alabaster) | [Page source](_sources/index.rst.txt)
