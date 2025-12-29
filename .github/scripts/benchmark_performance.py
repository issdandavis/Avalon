#!/usr/bin/env python3
"""
Performance Benchmarking Tool
Measures execution time of validation and analysis scripts
"""

import time
import subprocess
import sys
from pathlib import Path
from typing import Callable, Dict, List

def measure_execution_time(func: Callable, *args, **kwargs) -> tuple:
    """Measure execution time of a function"""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, (end - start) * 1000  # Convert to milliseconds

def benchmark_script(script_path: Path, description: str) -> Dict:
    """Benchmark a Python script"""
    print(f"\n⏱️  Benchmarking: {description}")
    print(f"   Script: {script_path.name}")
    
    times = []
    for i in range(3):
        start = time.perf_counter()
        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                cwd=script_path.parent.parent.parent,
                timeout=30
            )
            end = time.perf_counter()
            elapsed = (end - start) * 1000
            times.append(elapsed)
            print(f"   Run {i+1}: {elapsed:.2f}ms")
        except subprocess.TimeoutExpired:
            print(f"   Run {i+1}: TIMEOUT (>30s)")
            return {"error": "timeout"}
        except Exception as e:
            print(f"   Run {i+1}: ERROR - {e}")
            return {"error": str(e)}
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    print(f"   ✅ Average: {avg_time:.2f}ms (min: {min_time:.2f}ms, max: {max_time:.2f}ms)")
    
    return {
        "avg": avg_time,
        "min": min_time,
        "max": max_time,
        "runs": times
    }

def main():
    """Run benchmarks on all optimization targets"""
    repo_root = Path.cwd()
    scripts_dir = repo_root / ".github" / "scripts"
    
    print("=" * 60)
    print("🚀 Performance Benchmark Suite")
    print("=" * 60)
    
    benchmarks = [
        (scripts_dir / "validate_choicescript.py", "ChoiceScript Validator"),
        (scripts_dir / "stat_analyzer.py", "Stat Analyzer"),
        (scripts_dir / "find_dead_ends.py", "Dead End Detector"),
    ]
    
    results = {}
    for script_path, description in benchmarks:
        if not script_path.exists():
            print(f"\n⚠️  Skipping {description}: Script not found")
            continue
        
        results[description] = benchmark_script(script_path, description)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Performance Summary")
    print("=" * 60)
    
    for name, data in results.items():
        if "error" in data:
            print(f"❌ {name}: {data['error']}")
        else:
            print(f"✅ {name}: {data['avg']:.2f}ms avg")
    
    print("\n💡 Tips for optimization:")
    print("   - Pre-compile regex patterns")
    print("   - Cache file system lookups")
    print("   - Use generators for large datasets")
    print("   - Minimize file I/O operations")
    print("   - Batch DOM updates in JavaScript")

if __name__ == "__main__":
    main()
